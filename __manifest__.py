# See LICENSE file for full copyright and licensing details.

{
    "name": "Gcs Signature",
    "version": "1.0.0",
    "author": "Geelani Consultancy & Solutions, Aseemuddin Kazi, Mohamed Sohil Inamdar",
    "website": "https://www.geelani.com",
    'description': """
        This module extends the functionality of Odoo 16 by adding a signature feature to the reports of Sale Orders, Quotations, Invoices, Purchase Orders, and Requests For Quotation. It allows users to update signatures and display them in these reports, with the option of positioning the signatures on the left.""",
    "category": "",
    "summary": "Signature in reports",
    'license': 'OPL-1',
    "sequence": "-1000",
    "depends": ['base', 'account', 'sale', 'purchase'],
    "data": [
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
    "application": True,
    "auto_install": False,
}
