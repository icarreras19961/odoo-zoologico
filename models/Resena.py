from odoo import models, fields, api
class Resena(models.Model):
    _name = 'zoologico.resena'
    _description = 'Reseñas a recintos del zoologico'
    correo = fields.Char(string='Email del visitante', required=True)
    recinto = fields.Many2one('zoologico.recinto',string="Recinto")
    comentario = fields.Text(string="Texto de la reseña")
    fecha = fields.Date(string="Fecha de reseña")

    @api.model
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.correo} - {record.fecha}"))
        return res