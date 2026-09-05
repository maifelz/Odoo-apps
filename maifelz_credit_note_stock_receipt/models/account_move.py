from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    warehouse_id = fields.Many2one('stock.warehouse', string='Return Warehouse')
    stock_picking_ids = fields.Many2many('stock.picking', string='Stock Pickings', copy=False)
    picking_count = fields.Integer(compute='_compute_picking_count')

    @api.depends('stock_picking_ids')
    def _compute_picking_count(self):
        for move in self:
            move.picking_count = len(move.stock_picking_ids)

    def action_post(self):
        # Call super first to post the move
        res = super(AccountMove, self).action_post()

        for move in self:
            # Check if it is a Credit Note (out_refund) and has a Return Warehouse selected
            if move.move_type == 'out_refund' and move.warehouse_id:
                # Filter for lines with storable products (is_storable is Odoo 17+ standard)
                # Fallback to checking detailed_type if is_storable is not available in specific context
                stock_lines = move.invoice_line_ids.filtered(lambda l: l.product_id.is_storable)

                if not stock_lines:
                    continue

                picking_type = move.warehouse_id.in_type_id
                if not picking_type:
                    continue

                # Prepare Picking Values
                picking_vals = {
                    'picking_type_id': picking_type.id,
                    'partner_id': move.partner_id.id,
                    'origin': move.name,
                    'location_id': move.partner_id.property_stock_customer.id,
                    'location_dest_id': picking_type.default_location_dest_id.id,
                    'move_type': 'direct',
                }
                picking = self.env['stock.picking'].create(picking_vals)
                move.stock_picking_ids = [(4, picking.id)]

                # Create Stock Moves
                for line in stock_lines:
                    self.env['stock.move'].create({
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.quantity,
                        'product_uom': line.product_uom_id.id,
                        'picking_id': picking.id,
                        'picking_type_id': picking_type.id,
                        'location_id': picking.location_id.id,
                        'location_dest_id': picking.location_dest_id.id,
                    })

                # Validate the picking availability and assign
                picking.action_confirm()
                picking.action_assign()
        
        return res

    def action_view_picking(self):
        self.ensure_one()
        action = self.env.ref('stock.action_picking_tree_all').read()[0]
        pickings = self.stock_picking_ids
        if len(pickings) > 1:
            action['domain'] = [('id', 'in', pickings.ids)]
        elif pickings:
            form_view = [(self.env.ref('stock.view_picking_form').id, 'form')]
            if 'views' in action:
                action['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
            else:
                action['views'] = form_view
            action['res_id'] = pickings.id
        else:
             action = {'type': 'ir.actions.act_window_close'}
        return action
