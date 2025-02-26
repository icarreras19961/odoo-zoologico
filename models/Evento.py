from odoo import models, fields, api
class Evento(models.Model):
    _name = 'zoologico.evento'
    _description = 'Eventos del zoologico'
    nombre = fields.Char(string='Nombre especie', required=True)
    fecha_inicio = fields.Date(string="Fecha de inicio", required=True)
    fecha_final= fields.Date(string="Fecha final", required=True)
    recinto = fields.Many2one("zoologico.recinto", string="Recinto del evento")
    dias_evento = fields.Integer(string="Duracion en dias", compute="_calcular_dias", readonly = True)


    @api.depends("fecha_inicio", "fecha_final")
    def _calcular_dias(self):
        for record in self:
            d1 = fields.Date.from_string(record.fecha_inicio)
            d2 = fields.Date.from_string(record.fecha_final)
            record.dias_evento = (d2 - d1).days




    @api.model
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.nombre} - {record.fecha_inicio} --> {record.fecha_final}"))
        return res