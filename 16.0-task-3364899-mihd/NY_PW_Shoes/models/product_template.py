from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ProductTemplate(models.Model):
    #inherit the product template model
    _inherit='product.template'
    
    #Pair per case field
    pair_per_case=fields.Integer(string="Pair per case")
    
    #Price per pair field
    price_per_pair= fields.Monetary(string="Price per pair", currency_field="currency_id")
    
    #Sales price field
    list_price=fields.Float(string="Sale Price",compute='_compute_sale_price')
    
    detailed_type = fields.Selection(selection_add=[('shoes','Shoes')], 
                            ondelete={'shoes': 'set product'},
                            help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
                            'A consumable product is a product for which stock is not managed.\n'
                            'A service is a non-material product you provide.\n'
                            'A shoes product is the product for NY PW store\n')

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['shoes'] = 'product'
        return type_mapping
    
    @api.depends('pair_per_case','price_per_pair')
    def _compute_sale_price(self):
        for record in self:
            
            #Raise Validation Error when pair per case <0
            if record.pair_per_case and record.pair_per_case<0: raise ValidationError("Number of pairs cannot be less than 0")
            
            #Raise Validation Error when price per pair <0
            if record.price_per_pair and record.price_per_pair<0: raise ValidationError("Price cannot be less than 0")
            
            #Case that pair per case and price per pair are input
            if record.pair_per_case and record.price_per_pair:
                record.list_price=record.pair_per_case* record.price_per_pair
            else:
                record.list_price=1.0