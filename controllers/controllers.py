# -*- coding: utf-8 -*-
# from odoo import http


# class Zoologico(http.Controller):
#     @http.route('/zoologico/zoologico/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zoologico/zoologico/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('zoologico.listing', {
#             'root': '/zoologico/zoologico',
#             'objects': http.request.env['zoologico.zoologico'].search([]),
#         })

#     @http.route('/zoologico/zoologico/objects/<model("zoologico.zoologico"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zoologico.object', {
#             'object': obj
#         })
