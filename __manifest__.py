{
    'name': 'App One',
    'version': '18.0.1.1',
    'depends': ["base", 'sale', 'account', 'mail', 'contacts'
                ],
    'summary': '''An erp for Real Estate ''',
    'description': '''Real Estate  Company''',
    'author': 'mohamed elmeslamey',
    'category': 'Company',
    'website': 'www.mohamed_elmeslamey@gmail.com',
    "maintainer": "mohamed elmeslamey tech ltd {info@elmeslamey.com}",
    'sequence': 1,

    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/base_menu.xml",
        "views/property_view.xml",
        "views/owner_view.xml",
        "views/tag_view.xml",
        "views/sale_order_view.xml",
        "views/res_partner_view.xml",
        "views/building_view.xml",
        "views/property_history_view.xml",
        "wizard/change_state_wizard_view.xml",
        "reports/property_report.xml",

    ],
    'assets': {
        'web.assets_backend': ['app_one/static/src/css/property.css',
                               'app_one/static/src/components/listView/listView.css',
                               'app_one/static/src/components/listView/listView.js',
                               'app_one/static/src/components/listView/listView.xml',]
    },
    'application': True, }
