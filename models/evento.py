from odoo import models, fields
class Evento(models.Model):
    _name = 'zoologico.evento'
    _description = 'Eventos del zoologico'
    nombre = fields.Char(string='Nombre', required=True)
    fecha_inicio = fields.Date(string='Fecha de inicio', required=True)
    fecha_final = fields.Date(string='Fecha de final', required=True)
    recinto = fields.Many2one('zoologico.recinto',string="Recinto")
    # precio_entrada = fields.Monetary(string="Precio de la entrada")
