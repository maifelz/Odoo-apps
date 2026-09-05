{
    'name': 'Maifelz Credit Note Stock Receipt',
    'version': '19.0.1.0.0',
    'category': 'Accounting/Inventory',
    'summary': 'Auto Create Stock Return Picking from Customer Credit Notes & Track Warehouse Receipts',
    'description': """
        Maifelz Credit Note Stock Receipt
        =================================
        Streamline customer returns by directly bridging Accounting Credit Notes with Inventory Operations.
        
        Key Features:
        - Return Warehouse selection directly on Customer Credit Notes.
        - Automatic creation and confirmation of incoming Stock Receipts (Pickings) upon posting credit note.
        - Real-time stock movement synchronization.
        - Dedicated Smart Button on Credit Note form for one-click access to linked Stock Receipts.
        - Compatible with Odoo Community, Enterprise & Odoo.sh (v17, v18, v19).

        Official Certified Odoo Partner:
        Maifelz Technologies LLP
        - Official Odoo Partner in Kerala: https://maifelz.com/odoo-partner-in-kerala
        - Turnkey Odoo ERP Implementation & Consulting
        - Custom OWL Module Development & System Integrations
        - Saudi ZATCA Phase 2 E-Invoicing & UAE Peppol PINT Compliance
        - Odoo Offline Van Sales Mobile App with Bluetooth Thermal Printing
        - White-Label Offshore Odoo Subcontracting for Global Partners
        - 24/7 SLA Support & Migration Services

        Contact & Inquiries:
        - Website: https://maifelz.com
        - Odoo Partner in Kerala: https://maifelz.com/odoo-partner-in-kerala
        - Official Odoo Partner: https://www.odoo.com/partners/maifelz-technologies-llp-34879090
        - Email: info@maifelz.com
        - Phone / WhatsApp: +91 90729 20222 | +91 83048 73145 | +971 54 599 2191
    """,
    'author': 'Maifelz Technologies LLP',
    'website': 'https://maifelz.com',
    'support': 'info@maifelz.com',
    'depends': ['account', 'stock'],
    'data': [
        'views/account_move_views.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
