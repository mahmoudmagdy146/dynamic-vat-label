{
    'name': 'Dynamic VAT Label for Partners',
    'version': '19.0.1.0.0',
    'summary': 'Auto-adjust VAT / Tax ID label based on partner type (Company, Individual, Foreign)',
    'description': """
                Dynamic VAT Label for Partners
                =============================
                
                Problem
                -------
                In many countries, different types of partners require different identification numbers:
                - Companies → VAT / Tax ID
                - Individuals → National ID
                - Foreign partners → Passport ID
                
                Odoo uses a single "VAT" field, which can be confusing for users.
                
                Solution
                --------
                This module automatically updates the label and placeholder of the VAT field based on the partner type, ensuring clarity and reducing data entry errors.
                
                Features
                --------
                - Dynamic label switching (VAT / National ID / Passport)
                - Works seamlessly in the Contacts form
                - No configuration required
                - Lightweight and fast
                
                Use Case
                --------
                Perfect for companies operating in regions where multiple identification systems are used.
                """,
    'category': 'Contacts',
    'author': 'Mahmoud Magdy',
    'website': 'https://github.com/mahmoudmagdy146',
    'license': 'LGPL-3',
    'depends': ['base', 'contacts'],
    'assets': {
        'web.assets_backend': [
            'dynamic_vat_label_partner/static/src/js/vat_label_patch.js',
        ],
    },
    'data': [
        'views/res_partner.xml',
    ],
    'price': 09.99,
    'currency': 'USD',
    'installable': True,
    'application': False,
}
