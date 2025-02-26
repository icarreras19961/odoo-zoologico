from odoo import models, fields, api
from datetime import datetime

class Animal(models.Model):
    _name = 'zoologico.animal'
    _descripcion = "Animales del Zoologico"

    nombre = fields.Char(string="Nombre", required=True)
    genero = fields.Selection([('macho','Macho'),('hembra','Hembra')],string="Genero",default='macho')
    informacion_extra = fields.Text(string="Informacion")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    especie = fields.Many2one("zoologico.especie",string="Especie",requierd=True)
    imagen = fields.Image(string="Imagen")
    edad = fields.Integer(string="Fecha en años", compute="_calcular_edad", readonly=True)
    
    @api.model
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.nombre}"))
        return res
    
    @api.depends('fecha_nacimiento')
    def _calcular_edad(self):
        for record in self:
            if record.fecha_nacimiento:
                fecha_nacimiento = fields.Date.from_string(record.fecha_nacimiento)
                fecha_actual = datetime.today()
                edad = fecha_actual.year - fecha_nacimiento.year
                if fecha_actual.month < fecha_nacimiento.month or (fecha_actual.month == fecha_nacimiento.month and fecha_actual.day < fecha_nacimiento.day):
                    edad -= 1
                record.edad = edad
            else:
                record.edad = 0