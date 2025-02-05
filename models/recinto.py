from odoo import models, fields
class Libro(models.Model):
    _name = 'zoologico.recinto'
    _description = 'Recintos que se encuentran en el zoologico'
    nombre = fields.Char(string='Nombre del recinto', required=True)
    informacion_extra = fields.Text(string="Informacion sobre el recinto")
    encargado = fields.Ma
    recinto = fields.Many2Many('zoologico.especie',string="Habitantes")



    # autor = fields.Many2one('biblioteca.autor',string='Autor', required=True)
    # categoria_ids = fields.Many2many('biblioteca.categoria',string='Categorias', required=True)

    # estado = fields.Selection([('disponible', 'Disponible'),('prestado', 'Prestado')], string='Estado', default='disponible')