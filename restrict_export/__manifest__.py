# -*- coding: utf-8 -*-
##############################################################################
#
# OdooBro - odoobro.contact@gmail.com
#
##############################################################################
{
    'name': 'Restrict Export Data',
    'version': '1.0',
    'category': 'OdooBro Apps',
    'description': """
This module restrict export data of users.
    """,
    'author': 'OdooBro',
    'website': 'http://www.odoobro.com',
    'depends': [
        'base',
        'web',
        'base_setup'
    ],
    'data': [
        'security/res_groups_data.xml',
        'view/base/restrict_export_view.xml',
        'view/base/base_config_settings_view.xml',
    ],

    'test': [],
    'demo': [],

    'installable': True,
    'active': False,
    'application': True,
}
