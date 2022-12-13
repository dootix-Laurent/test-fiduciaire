# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError


class AccountJournal(models.Model):
    _inherit = "account.journal"

    def create_iso20022_credit_transfer(self, payments, batch_booking=False, sct_generic=False):
        if self._context.get('active_model') == 'hr.payslip.run':
            for payment in payments:
                slip = self.env['hr.payslip'].browse(payment['id'])
                payment['payment_date'] = slip.payslip_run_id.payment_date
        return super(AccountJournal, self).create_iso20022_credit_transfer(payments=payments, batch_booking=batch_booking, sct_generic=sct_generic)
