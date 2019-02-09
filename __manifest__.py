# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'ALDALEEL GPS',
    'version': '0.1',
    'category': 'Tools',
    'summary': 'This application integrates and displays data from ALDALEEL GPS backend',
    'depends': ['web'],
    'data': [
        'data/actions.xml',
        'data/location_views.xml',
    ],
    'demo': [
    ],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
