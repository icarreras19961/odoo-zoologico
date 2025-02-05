from odoo import models, fields
class Libro(models.Model):
    _name = 'zoologico.especie'
    _description = 'Especies que se encuentran en el zoologico'
    nombre = fields.Char(string='Nombre especie', required=True)
    informacion_extra = fields.Text(string="Informacion sobre la especie")
    clase = fields.Selection([('anfibios', 'anfibios'),('mamifero', 'mamifero'),('reptiles', 'reptiles'),('peces', 'peces'),('aves', 'aves'),('insectos', 'insectos'),('artrópodos', 'artrópodos'),('crustáceos', 'crustáceos'),('moluscos', 'moluscos'),('arácnidos', 'arácnidos'),('anélidos ', 'anélidos '),('gasterópodos', 'gasterópodos')], string='Clase de animal', default='mamifero')
    animales_asociados = fields.One2many('zoologico.animal', 'especie', String="Animales asociados")
    recinto = fields.Many2one('zoologico.recinto',string="Recinto")
