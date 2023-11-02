# -*- coding: utf-8 -*-
# from odoo import http


# class Dev-test(http.Controller):
#     @http.route('/dev-test/dev-test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dev-test/dev-test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dev-test.listing', {
#             'root': '/dev-test/dev-test',
#             'objects': http.request.env['dev-test.dev-test'].search([]),
#         })

#     @http.route('/dev-test/dev-test/objects/<model("dev-test.dev-test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dev-test.object', {
#             'object': obj
#         })
