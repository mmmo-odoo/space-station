{
    'name' : 'Space Station',
    'version' : '1.0',
    'author': "Mayank Mangal Mourya",
    'summary' : 'Track Real Time Requirements For Astronauts',
    'description' : """
        space station management project involves creating a comprehensive ERP system to efficiently
        manage various aspects of a space station, including astronaut requirements, manufacturing 
        processes, inventory management, and invoicing. The modular structure facilitates the tracking 
        of astronaut essentials, production orders, and stock levels while streamlining invoicing 
        procedures. The user-friendly interface and customized workflows enhance usability, and 
        integrated reporting provides insights into the project's different facets. The project aims 
        to optimize operations and ensure the smooth functioning of the space station through effective 
        resource planning and management.
    """,
    'depends' : [
        'base',
        'product',
    ],
    'data' : [
        'security/ir.model.access.csv',
        'views/station_product_view.xml',
        'views/station_modules_view.xml',
        'views/station_organization_view.xml',
        'views/station_astronauts_view.xml',
        'views/station_property_view.xml',
        'views/station_property_menu.xml',
    ],
    'demo' : [
        'demo/station.organization.csv',
        'demo/station.detail.xml',
        'demo/station.astronauts.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license':'LGPL-3',
}