from odoo import models, fields, api

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    serial_number = fields.Char(string='Serial Number', readonly=True, copy=False, default='New')

    @api.model
    def create(self, vals):
      if vals.get('serial_number', 'New') == 'New':
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('crm.lead.serial') or '/'
      return super(CrmLead, self).create(vals)