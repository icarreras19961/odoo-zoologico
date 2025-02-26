from odoo import models, fields, api
class Inventario(models.Model):
    _name = 'zoologico.inventario'
    _description = 'Iventario del zoologico'
    item = fields.Char(string='Nombre del item', required=True)
    stock = fields.Integer(string="Cantidad de stock")


    @api.model
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.item}"))
        return res