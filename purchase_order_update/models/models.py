# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"

    state = fields.Selection([
        ('draft', 'Employee'),
        ('sent', 'RFQ Sent'),
        ('direct_manager', 'Direct Manager'),
        ('department_manager', 'Department Manager'),
        ('general_manager', 'General Manager'),
        ('concerned_department', 'Concerned Department'),
        ('purchase_department', 'Purchase Department'),
        ('to approve', 'To Approve'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
    ], string='Status', readonly=True, index=True, copy=False, default='draft', track_visibility='onchange')

    def employee_approval(self):
        self.state = 'direct_manager'

    def direct_manager_approval(self):
        self.state = 'department_manager'

    def department_manager_approval(self):
        self.state = 'general_manager'

    def general_manager_approval(self):
        self.state = 'concerned_department'

    def concerned_department_approval(self):
        self.state = 'purchase_department'

    @api.multi
    def button_confirm(self):
        for order in self:
            if order.state not in ['purchase_department', 'sent']:
                continue
            order._add_supplier_to_product()
            # Deal with double validation process
            if order.company_id.po_double_validation == 'one_step' \
                    or (order.company_id.po_double_validation == 'two_step' \
                        and order.amount_total < self.env.user.company_id.currency_id._convert(
                        order.company_id.po_double_validation_amount, order.currency_id, order.company_id,
                        order.date_order or fields.Date.today())) \
                    or order.user_has_groups('purchase.group_purchase_manager'):
                order.button_approve()
            else:
                order.write({'state': 'to approve'})
        return True