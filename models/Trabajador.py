from odoo import models, fields, api
class Trabajador(models.Model):
    _name = 'zoologico.trabajador'
    _description = 'Trabajadores del zoologico'
    nombre = fields.Char(string='Nombre y apellidos', required=True)
    dni = fields.Char(string="DNI", required=True)
    informacion_extra = fields.Text(string="Informacion sobre el trabajador")
    estado = fields.Selection([('t', 'Trabajando'),('b', 'De baja'),('v', 'En vacaciones'),('d', 'Despedido')], string='Estado', default='t')
    recintos = fields.Many2many('zoologico.recinto', string="Recintos")


    @api.model
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.nombre} - {record.dni}"))
        return res