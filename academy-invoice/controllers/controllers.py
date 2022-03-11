# -*- coding: utf-8 -*-
# from odoo import http


# class Academy-invoice(http.Controller):
#     @http.route('/academy-invoice/academy-invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy-invoice/academy-invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy-invoice.listing', {
#             'root': '/academy-invoice/academy-invoice',
#             'objects': http.request.env['academy-invoice.academy-invoice'].search([]),
#         })

#     @http.route('/academy-invoice/academy-invoice/objects/<model("academy-invoice.academy-invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy-invoice.object', {
#             'object': obj
#         })
