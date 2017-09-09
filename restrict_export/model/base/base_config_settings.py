# -*- coding: utf-8 -*-
##############################################################################
#
# OdooBro - odoobro.contact@gmail.com
#
##############################################################################
from odoo import fields, models


class BaseConfigSettings(models.TransientModel):
    _inherit = 'base.config.settings'

    restrict_models = fields.Char(
        string='Restrict Export Models',
        help="Restrict Models: For example sale.order,purchase.order")

    def set_restrict_models(self):
        ir_values_obj = self.env['ir.values']
        ir_values_obj.sudo().set_default(
                'base.config.settings', "restrict_models",
                self.restrict_models)
