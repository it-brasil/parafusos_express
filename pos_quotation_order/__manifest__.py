{
    'name': "POS - Pedidos",
    'version': '12.0.1.0.0',
    'summary': """Create & Process Quotation from POS""",
    'description': """This module allows to create and process quotation orders from POS.""",
    'category': 'Point of Sale',
    'depends': ['point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/quotation_templates.xml',
        'views/pos_quotation.xml',
        'report/pos_quotation.xml',
    ],
    'qweb': ['static/src/xml/pos_quotation.xml'],
}
