# -*- coding: utf-8 -*-
# Copyright 2017 Open Net Sàrl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Switzerland - Dootix Payroll',
    'summary': 'Switzerland Payroll Rules',
    'category': 'Localization',
    'author': "Dootix Sarl",
    'depends': [
        'hr_payroll_account',
        'hr_contract',
        'hr_attendance',
        'hr_payroll_account_sepa',
    ],
    'version': '15.0.1',
    'auto_install': False,
    'demo': [],
    'website': 'http://www.dootix.com',
    'license': 'AGPL-3',
    'data': [
        'views/hr_contract_view.xml',
        'views/hr_payslip_run.xml',
    ],
    'installable': True
}
