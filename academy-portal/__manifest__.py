# -*- coding: utf-8 -*-
{
    'name': "Academy Portal",

    'summary': """
        El portal de la academia le permitara a los estudiantes tener acceso a la plataforma
        para tomar clases en linea y ver sus asigturadas seleccionadas.
        
        Podra manejar videoconferencia y entregar sus trabajos a traves de las tareas habilitada
        en el portal del estudiante.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "STARLEAN",
    'website': "http://www.starlean.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['academy'],

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
