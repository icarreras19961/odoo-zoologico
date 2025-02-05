from odoo import models, fields
class Libro(models.Model):
    _name = 'zoologico.animal'
    _description = 'Animales individuales del zoologico'
    nombre = fields.Char(string='Nombre', required=True)
    genero = fields.Selection([('m', 'Macho'),('f', 'Hembra')], string='Genero', default='f')
    informacion_extra = fields.Text(string="Informacion sobre el animal")
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    especie = fields.Many2one('zoologico.especie',string="Especie")



    # autor = fields.Many2one('biblioteca.autor',string='Autor', required=True)
    # categoria_ids = fields.Many2many('biblioteca.categoria',string='Categorias', required=True)

    # estado = fields.Selection([('disponible', 'Disponible'),('prestado', 'Prestado')], string='Estado', default='disponible')