# -*- coding: utf-8 -*-
{
    'name': 'Health_Care',
    'version': '17.0.1.0',
    'description': """ Health_Care Description """,
    'summary': """ Health_care Summary """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web'],
    'data': [ 
        'security/ir.model.access.csv',
        
        'views/hc_contact_views.xml',
        'views/hc_contact_relation_views.xml',

        'views/hc_certification_views.xml',
        
        'views/hc_patient_views.xml',
        'views/hc_patient_contact_views.xml',
        'views/hc_patient_insurance_views.xml',
        'views/hc_patient_import_views.xml',

        'views/hc_physician_views.xml',
        
        'views/hc_nurse_views.xml',
        'views/hc_nurse_category_views.xml',
        'views/hc_nurse_certification.xml',

        'views/hc_visit_views.xml',
        'views/hc_visit_type_views.xml',
       
        'views/hc_medicine_views.xml',
        'views/hc_medicine_family_views.xml',

        'views/hc_intake_views.xml',
 

        'views/hc_discipline_views.xml',
        'views/hc_diagnostic_views.xml',
        
        'views/hc_intake_diagnostic_views.xml',
        'views/hc_intake_medicine_views.xml',
        'views/hc_intake_discipline_views.xml',


        'views/hc_facility_views.xml',
        'views/hc_limitation_views.xml',

        'views/hc_menuitem.xml',
    ],
    'assets': {

    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
