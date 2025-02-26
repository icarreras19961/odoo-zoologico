from odoo import models, fields, api
class Recinto(models.Model):
    _name = 'zoologico.recinto'
    _description = 'Recintos del zoologico'
    nombre = fields.Char(string='Nombre del recinto', required=True)
    informacion_extra = fields.Text(string="Informacion sobre el recinto")
    trabajador = fields.Many2many('zoologico.trabajador', string="Encargados")
    especies = fields.One2many('zoologico.especie','recinto',string="Habitantes")


    @api.model
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.nombre}"))
        return res