from odoo import models, fields, api


class GcsSale(models.Model):
    _inherit = 'sale.order'

    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id)
    type_of_signature = fields.Char(string='Type of Signature',
                                    default=lambda self: self.env["res.config.settings"].get_setting()[
                                        'signature_option'])
    is_sale_order = fields.Boolean(string='Is Sale Order',
                                   default=lambda self: self.env["res.config.settings"].get_sale_order())

    signature_position = fields.Boolean(string='Signature Position At Left',
                                        default=lambda self: self.env["res.config.settings"].get_signature_position())

    @api.model
    def default_get(self, fields):
        res = super(GcsSale, self).default_get(fields)
        settings = self.env["res.config.settings"]
        signature_option = settings.get_setting()['signature_option']
        is_sale_order = settings.get_sale_order()
        signature_position = settings.get_signature_position()
        for rec in self:
            rec.type_of_signature = signature_option
            rec.is_sale_order = is_sale_order
            rec.signature_position = signature_position
        return res
