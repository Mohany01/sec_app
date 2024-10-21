from email.policy import default

from odoo import models, fields
from odoo.odoo.fields import One2many


class Owner(models.Model):
    _name = 'owner'

    name = fields.Char(required=1, default='New')
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.One2many("property", "owner_id")



