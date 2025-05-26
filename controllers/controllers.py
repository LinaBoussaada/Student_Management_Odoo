# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolManagment(http.Controller):
#     @http.route('/school_managment/school_managment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_managment/school_managment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_managment.listing', {
#             'root': '/school_managment/school_managment',
#             'objects': http.request.env['school_managment.school_managment'].search([]),
#         })

#     @http.route('/school_managment/school_managment/objects/<model("school_managment.school_managment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_managment.object', {
#             'object': obj
#         })
