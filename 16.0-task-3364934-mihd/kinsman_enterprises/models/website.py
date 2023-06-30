from odoo import fields, api,models

class Website(models.Model):
    _inherit='website'
    
    is_hide_price=fields.Boolean(string="Hide price")