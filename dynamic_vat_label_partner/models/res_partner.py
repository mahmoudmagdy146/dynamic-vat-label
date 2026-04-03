# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_

class ResPartner(models.Model):
    _inherit='res.partner'

    person_type = fields.Selection(selection=[('B', 'Business'), ('P', 'Natural Person'), ('F', 'Foreigner')], string="Person Type", default='B')

    @api.depends_context('company','person_type')
    def _compute_vat_label(self):
        self.vat_label = _("Tax ID") if self.person_type == 'B' else _("National ID") if self.person_type == 'P' else _("Passport ID")