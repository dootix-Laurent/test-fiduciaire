# -*- coding: utf-8 -*-
# Copyright 2017 Open Net Sàrl
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api
import odoo.addons.decimal_precision as dp


class HrContract(models.Model):
    _inherit = 'hr.contract'

    lpp_amount_company = fields.Float(string='Montant LPP entreprise')
    lpp_amount_employee = fields.Float(string='Montant LPP employé')
    imp_src = fields.Float(string="Impôts à la  source")
    familiy_allowances = fields.Float(string="Allocations familiales")
    other_expenses = fields.Float(string="Autres frais forfaitaires")
    car_part = fields.Float(string="Part privée aux frais de véhicule")
