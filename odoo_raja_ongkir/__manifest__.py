# -*- coding: utf-8 -*-
{
    "name": "Odoo Raja Ongkir Integration",
    "author": "Byron Josafat Martinelli",
    "website": "https://www.linkedin.com/in/byron-josafat-martinelli-916877219",
    "version": "16.0.0.0",
    "depends": [
        'base','web','website','sale','delivery', 'website_sale_delivery',
    ],
    "data": [
        'security/ir.model.access.csv',
        'view/setting.xml',
        'view/template.xml',
        'data/data.xml',
    ],
    "qweb": [],
    'assets': {
        'web.assets_frontend': [
            'odoo_raja_ongkir/static/src/js/delivery.js',
            'odoo_raja_ongkir/static/src/css/custom.css',
        ],
    },
    'images': ['images/cover.png'],
    "license": 'OPL-1',
    'installable': True
}