from odoo import models, fields, api


class GcsPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id)
    type_of_signature = fields.Char(string='Type of Signature', compute='_compute_default_values')

    is_purchase_order = fields.Boolean(string='Is Purchase Order', compute='_compute_default_values')
    request_for_quotation = fields.Boolean(string='Is Request For Quotation', compute='_compute_default_values')

    signature_position = fields.Boolean(string='Signature Position At Left', compute='_compute_default_values')

    @api.onchange('id')
    def _compute_default_values(self):
        settings = self.env["res.config.settings"]
        signature_option = settings.get_setting()['signature_option']
        signature_position = settings.get_signature_position()
        is_purchase_order = settings.get_purchase_order()
        request_for_quotation = settings.get_request_for_quotation()
        for record in self:
            record.type_of_signature = signature_option
            record.is_purchase_order = is_purchase_order
            record.request_for_quotation = request_for_quotation
            record.signature_position = signature_position
