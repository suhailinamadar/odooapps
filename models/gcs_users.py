from odoo import models, fields


class GcsResUsers(models.Model):
    _inherit = 'res.users'

    gcs_signature = fields.Binary(string='Signature', store=True)
