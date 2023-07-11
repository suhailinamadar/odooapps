from odoo import models, fields, api


# the below class is created for inheriting the res.company
class GcsCompany(models.Model):
    _inherit = 'res.company'

    signature = fields.Binary(string='Signature', store=True)