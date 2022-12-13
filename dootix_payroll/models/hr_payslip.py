# -*- coding: utf-8 -*-
# Copyright 2017 Open Net Sàrl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64
import odoo.addons.decimal_precision as dp
from datetime import timedelta, datetime, date
from odoo import fields, models, api, _
from odoo.exceptions import UserError

# Import logger
import logging

# Get the logger
_logger = logging.getLogger(__name__)


class HrPayslip(models.Model):

    _inherit = 'hr.payslip'

    current_month = fields.Integer("Current month", compute="_get_current_month")
    other_year_payslip_ids = fields.Many2many('hr.payslip', string="Autres salaires de l'années", compute="_get_other_payslips")

    def _get_other_payslips(self):
        for payslip in self:
            if payslip.date_from is not False:
                current_year = fields.Date.from_string(payslip.date_from).year
                date_from = "%s-01-01" % current_year
                date_to = "%s-12-31" % current_year
                other_payslips = self.search([
                    ('employee_id', '=', payslip.employee_id.id),
                    ('id', '!=', payslip.id),
                    ('date_from', '>=', date_from),
                    ('date_to', '<=', date_to)
                ])
                payslip.other_year_payslip_ids = other_payslips

    def get_number_of_payslips_unique_per_month(self):
        total = 0
        months = set()
        for other_payslip in self.other_year_payslip_ids:
            month = fields.Date.from_string(other_payslip.date_from).month
            if month not in months:
                months.add(month)
                total += 1
        if self.date_from is not False:
            month = fields.Date.from_string(self.date_from).month
            if month not in months:
                months.add(month)
                total += 1
        return total

    def get_total_of_rule_by_code(self, code, amount):
        total = 0
        for other_payslip in self.other_year_payslip_ids:
            total += sum([line.total for line in other_payslip.line_ids if line.code == code])
        total += amount
        return total

    def _get_current_month(self):
        for payslip in self:
            if payslip.date_from is not False:
                payslip.current_month = fields.Date.from_string(payslip.date_from).month
            else:
                payslip.current_month = date.today().month
