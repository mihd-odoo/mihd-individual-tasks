from odoo import fields,models,api

class ProductTemplate(models.Model):
    _inherit='product.template'
    
    product_group=fields.Selection(readonly=False,required=True,
                                   selection=[('0111','Product 1'),
                                        ('0222','Product 2'),
                                        ('0333','Product 3'),], store=True)
    
    store_barcode_sequence=fields.Char(string="temp")
    
    @api.depends('product_group')
    def _compute_barcode(self):
        for template in self:
            if template.product_group:
                if not template.store_barcode_sequence:
                    template.store_barcode_sequence=self.env['ir.sequence'].next_by_code('matrix.sequence')
                template.barcode=template.product_group[:2]+'.'+template.store_barcode_sequence