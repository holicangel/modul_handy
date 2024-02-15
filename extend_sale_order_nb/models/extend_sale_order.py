from odoo import models, fields

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    commitment_date = fields.Date(string='Delivery Date', required=False)
