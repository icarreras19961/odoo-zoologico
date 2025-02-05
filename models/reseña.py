from odoo import models, fields
class Libro(models.Model):
    _name = 'zoologico.reseña'
    _description = 'Reseñas a recintos del zoologico'
    correo = fields.Char(string='Email del visitante', required=True)
    