
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    custo_reposicao = fields.Monetary(string="Custo de Reposição")