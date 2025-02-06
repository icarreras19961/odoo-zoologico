from odoo import models, fields
class Inventario(models.Model):
    _name = 'zoologico.Inventario'
    _description = 'Iventario del zoologico'
    item = fields.Char(string='Nombre del item', required=True)
    stock = fields.Integer(string="Cantidad de stock")   