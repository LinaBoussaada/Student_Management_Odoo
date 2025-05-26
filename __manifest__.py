
{
    'name': "School management",

    'summary': "This module allows you to manage a school",

    'description': "This module allows you to manage a school",

    'author': "Lina Boussaada",
    'website': "https://www.yourcompany.com",

    'category': 'Education',
    'version': '1.0',

    
    'depends': ['base','mail','web'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/student_view.xml',
        'security/ir.model.access.csv',
        'views/student_class_view.xml', 
        'views/school_course_view.xml',       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'auto_install': False,
    'application': False,
    'sequence': '0',
    'images': ['static/description/icon.png'],
    
}
