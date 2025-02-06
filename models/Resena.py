from odoo import models, fields
class Resena(models.Model):
    _name = 'zoologico.resena'
    _description = 'Reseñas a recintos del zoologico'
    correo = fields.Char(string='Email del visitante', required=True)
    recinto = fields.Many2one('zoologico.recinto',string="Recinto")
    comentario = fields.Text(string="Texto de la reseña")