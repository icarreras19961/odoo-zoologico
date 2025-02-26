from odoo import models, fields, api
class Especie(models.Model):
    _name = 'zoologico.especie'
    _description = 'Especies del zoologico'
    
    nombre = fields.Char(string='Nombre', required=True)
    informacion_extra = fields.Text(string="Informacion sobre la especie")
    clase = fields.Selection([('anfibios', 'anfibios'),('mamifero', 'mamifero'),('reptiles', 'reptiles'),('peces', 'peces'),('aves', 'aves'),('insectos', 'insectos'),('artropodos', 'artrópodos'),('crustaceos', 'crustáceos'),('moluscos', 'moluscos'),('aracnidos', 'arácnidos'),('anelidos', 'anélidos'),('gasteropodos', 'gasterópodos')], string='Clase de animal', default='mamifero')
    animales_asociados = fields.One2many('zoologico.animal', 'especie', string="Animales asociados")
    recinto = fields.Many2one('zoologico.recinto',string="Recinto")

    @api.model
    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f"{record.nombre}"))
        return res