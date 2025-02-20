from odoo import models, fields

class Animal(models.Model):
    _name = 'zoologico.animal'
    _descripcion = "Animales del Zoologico"

    nombre = fields.Char(string="Nombre", required=True)
    genero = fields.Selection([('macho','Macho'),('hembra','Hembra')],string="Genero",default='macho')
    informacion_extra = fields.Text(string="Informacion")
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    especie = fields.Many2one("zoologico.especie",string="Especie",requierd=True)
    imagen = fields.Image(string="Imagen")