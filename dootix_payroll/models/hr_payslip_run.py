# -*- coding: utf-8 -*-

from odoo import models, fields


class HrPayslipRun(models.Model):
    _inherit = 'hr.payslip.run'

    payment_date = fields.Date(string="Payment Date")
