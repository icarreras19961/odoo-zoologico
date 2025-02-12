# -*- coding: utf-8 -*-
{
    'name': "zoologico",

    'summary': """
        Modulo para el manejo de un zoologico""",

    'description': """
        Un modulo sobre un zoologico
    """,
    'installable':True,
    'author': "Daniel Ibarra, Ivan Carreras",
    'website': "https://github.com/dibarra19976/odoo-zoologico",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/inventario_view.xml',
        'views/Resena_view.xml',
        'views/Trabajador_view.xml',
        'views/Recinto_view.xml',
        'views/Especie_view.xml',
        'views/Animal_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
