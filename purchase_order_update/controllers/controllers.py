# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseOrderUpdate(http.Controller):
#     @http.route('/purchase_order_update/purchase_order_update/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_order_update/purchase_order_update/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_order_update.listing', {
#             'root': '/purchase_order_update/purchase_order_update',
#             'objects': http.request.env['purchase_order_update.purchase_order_update'].search([]),
#         })

#     @http.route('/purchase_order_update/purchase_order_update/objects/<model("purchase_order_update.purchase_order_update"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_order_update.object', {
#             'object': obj
#         })
