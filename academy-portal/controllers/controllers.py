# -*- coding: utf-8 -*-
# from odoo import http


# class Academy-portal(http.Controller):
#     @http.route('/academy-portal/academy-portal/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy-portal/academy-portal/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy-portal.listing', {
#             'root': '/academy-portal/academy-portal',
#             'objects': http.request.env['academy-portal.academy-portal'].search([]),
#         })

#     @http.route('/academy-portal/academy-portal/objects/<model("academy-portal.academy-portal"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy-portal.object', {
#             'object': obj
#         })
