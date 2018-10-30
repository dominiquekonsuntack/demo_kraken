##############################################################################
#
# Copyright (c) 2017 Modoolar (http://modoolar.com) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract support@modoolar.com
#
##############################################################################
{
    'name': "Netability",
    'summary': "Custom Module for Netability",
    'category': 'CRM, Sale Orders',
    'version': '11.0.1.0.0',
    'author': "Modoolar",
    'website': "http://www.modoolar.com",
    'depends': [
        'account_accountant',
        'crm',
        'sale_margin',
        'helpdesk_timesheet',
        'website_helpdesk',
        'website',
        'website_crm_partner_assign',
        'sale_subscription',
        'timesheet_products',
        'sale',
    ],
    'data': [
        'data/stage.xml',
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/crm_opportunity.xml',
        'views/account_invoice_report.xml',
        # 'views/portal_templates.xml',
        'views/account_analytic_line.xml',
        # 'views/webclient_templates.xml',
    ],
    # 'qweb': ['static/src/xml/website.backend.xml'],

}
