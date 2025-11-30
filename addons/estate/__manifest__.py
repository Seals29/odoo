{
    'name': 'Estate Module',
    'version': '1.0',
    'summary': 'Simple estate module',
    'category': 'Real Estate',
    'depends': ['base'],
    'data': [
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_menus.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
