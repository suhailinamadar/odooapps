# -*- coding: utf-8 -*-
{
    'name': 'Gcs Signature',
    'version': '1.0.0',
    'summary': 'Odoo 16 Signature Model',
    'sequence': -100,
    'description': """Odoo 16""",
    'category': 'Tutorials',
    'author': 'Geelani',
    'maintainer': 'Geelani',
    'website': 'https://www.geelani.com',
    'depends': [
        'base', 'account', 'sale', 'purchase'
    ],
    'data': [
      "views/gcs_res_company.xml",
        "views/gcs_invoice.xml",
        "views/gcs_sales.xml",
        "views/gcs_purchase_order.xml",
        "views/gcs_setting.xml",
        "views/gcs_users.xml",
        "reports/gcs_sale_order.xml",
        "reports/gcs_invoice_report.xml",
        "reports/gcs_purchase_order_report.xml",
        "reports/gcs_rfq_report.xml",
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
