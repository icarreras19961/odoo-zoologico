from odoo import models, fields
class Recinto(models.Model):
    _name = 'zoologico.recinto'
    _description = 'Recintos del zoologico'
    nombre = fields.Char(string='Nombre del recinto', required=True)
    informacion_extra = fields.Text(string="Informacion sobre el recinto")
    trabajador = fields.Many2many('zoologico.trabajador', string="Encargados")
    especies = fields.One2many('zoologico.especie','recinto',string="Habitantes")