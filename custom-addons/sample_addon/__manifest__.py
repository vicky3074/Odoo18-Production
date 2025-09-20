# -*- coding: utf-8 -*-
{
    'name': 'Sample Custom Addon',
    'version': '18.0.1.0.0',
    'category': 'Tools',
    'summary': 'A sample custom addon for development',
    'description': """
        This is a sample custom addon to demonstrate
        the development environment setup.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/sample_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}