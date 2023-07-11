from odoo import fields, models, api
import os


class GcsSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    signature_option = fields.Selection(
        selection=[('company_signature', 'Company Signature'), ('individual_signature', 'Individual Signature')],
        string='Signature Option',
        config_parameter='directory.path.signature_option'
    )
    sale_order = fields.Boolean(string='Sale Order', config_parameter='directory.path.sale_order_option')
    invoice = fields.Boolean(string='Invoice', config_parameter='directory.path.invoice')
    purchase_order = fields.Boolean(string='Purchase Order', config_parameter='directory.path.purchase_order')
    request_for_quotation = fields.Boolean(string='Request For Quotation',
                                           config_parameter='directory.path.request_for_quotation')
    signature_position = fields.Boolean(string='Signature Position At Left',
                                        config_parameter='directory.path.signature_position')

    def _get_settings(self, param_name, os_var_name):
        config_obj = self.env["ir.config_parameter"]
        res = config_obj.sudo().get_param(param_name)
        if not res:
            res = os.environ.get(os_var_name)
        return res

    def get_setting(self):
        signature_option = self._get_settings("directory.path.signature_option", "Signature")
        settings = {
            'signature_option': signature_option,
        }
        return settings

    def get_sale_order(self):
        sale_order = self._get_settings("directory.path.sale_order_option", "Sale Order")
        return sale_order

    def get_invoice(self):
        invoice = self._get_settings("directory.path.invoice", "Invoice")
        return invoice

    def get_purchase_order(self):
        purchase_order = self._get_settings("directory.path.purchase_order", "Purchase Order")
        return purchase_order

    def get_request_for_quotation(self):
        request_for_quotation = self._get_settings("directory.path.request_for_quotation", "Request For Quotation")
        return request_for_quotation

    def get_signature_position(self):
        signature_position = self._get_settings("directory.path.signature_position", "Signature Position At Left")
        return signature_position

    @api.model
    def get_values(self):
        res = super(GcsSettings, self).get_values()
        signature_option = self.env["ir.config_parameter"].sudo().get_param("directory.path.signature_option",
                                                                            default="")
        sale_order = self.env["ir.config_parameter"].sudo().get_param("directory.path.sale_order_option")
        invoice = self.env["ir.config_parameter"].sudo().get_param("directory.path.invoice")
        purchase_order = self.env["ir.config_parameter"].sudo().get_param("directory.path.purchase_order")
        request_for_quotation = self.env["ir.config_parameter"].sudo().get_param("directory.path.request_for_quotation")
        signature_position = self.env["ir.config_parameter"].sudo().get_param("directory.path.signature_position")

        res.update(
            signature_option=signature_option,
            sale_order=sale_order,
            invoice=invoice,
            purchase_order=purchase_order,
            request_for_quotation=request_for_quotation,
            signature_position=signature_position,
        )
        return res

    def set_values(self):
        super(GcsSettings, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param("directory.path.signature_option", self.signature_option or "")
        self.env["ir.config_parameter"].sudo().set_param("directory.path.sale_order_option",
                                                         self.sale_order)
        self.env["ir.config_parameter"].sudo().set_param("directory.path.invoice", self.invoice)
        self.env["ir.config_parameter"].sudo().set_param("directory.path.purchase_order", self.purchase_order)
        self.env["ir.config_parameter"].sudo().set_param("directory.path.request_for_quotation",
                                                         self.request_for_quotation)
        self.env["ir.config_parameter"].sudo().set_param("directory.path.signature_position",
                                                         self.signature_position)
