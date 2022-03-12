# -*- coding: utf-8 -*-
{
    'name': "Academy",

    'summary': """
    Este aplicacion le permitara gestionar los procesos de un centros de educacion, Universidad
    y Escuelas de nivel primaria y secundaria.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "STARLEAN",
    'website': "http://www.starlean.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Apps',
    'version': '0.1',
    'application': 'True',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
