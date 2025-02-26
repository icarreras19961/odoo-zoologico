from odoo import models, fields
class Evento(models.Model):
    _name = 'zoologico.evento'
    _description = 'Eventos del zoologico'
    nombre = fields.Char(string='Nombre especie', required=True)
    fecha_inicio = fields.Date(string="Fecha de inicio", required=True)
    fecha_final= fields.Date(string="Fecha final", required=True)
    recinto = fields.Many2one("zoologico.recinto", string="Recinto del evento")
    # dias_evento = fields.Integer(string="Duracion en dias", compute="_calcular_dias", Store=True)


    # @api.depends()
    # def _calcular_dias(self):
    #     for record in self:
    #         fmt = '%Y-%m-%d'
    #         d1 = datetime.strptime(record.fecha_inicio, fmt)
    #         d2 = datetime.strptime(record.fecha_final, fmt)
    #         record.dias_evento = d2 - d1