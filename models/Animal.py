from odoo import models, fields

class Animal(models.Model):
    _name = 'zoologico.animal'
    _descripcion = "Animales del Zoologico"

    nombre = fields.Char(string="Nombre", required=True)
    genero = fields.Selection([('macho','Macho'),('hembra','Hembra')],string="Genero",default='macho')
    informacion_extra = fields.Text(string="informacion")
    fecha_nacimiento = fields.Date(string="fecha nacimiento", required=True)
    especie = fields.Many2one(string="especie",requierd=True)
    imagen = fields.Image(string="Imagen")