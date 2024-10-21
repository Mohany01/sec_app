from email.policy import default

from odoo import models, fields
from odoo.odoo.fields import One2many


class Tag(models.Model):
    _name = 'tag'

    name = fields.Char(required=1, default='New')




