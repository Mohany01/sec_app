from email.policy import default

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(required=1, default='New')
    description = fields.Text(track_visibility='always')
    postcode = fields.Char(required=1, size=4)
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff', store=1)
    bedrooms = fields.Integer(size=1)
    living_area = fields.Integer(size=1)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(size=3)
    owner_id = fields.Many2one("owner", required=1)
    tag_ids = fields.Many2many("tag")
    line_ids = fields.One2many("property.line", "property_id")
    owner_phone = fields.Char(related='owner_id.phone')
    owner_address = fields.Char(related='owner_id.address')

    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('west', 'West'),
        ('east', 'East'),
    ])
    status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold')
    ] ,default="draft")
    _sql_constraints = [
        ('unique_name', 'unique("name")', 'This Name Already is Exist'),
        ('unique_postcode', 'unique("postcode")', 'This postcode is Already Exist')

    ]
    @api.depends('selling_price','expected_price','owner_id.phone')
    def _compute_diff(self):
        for rec in self:
            print(rec)
            rec.diff =  rec.expected_price - rec.selling_price


    @api.constrains('garden')
    def _check_garden(self):
        for rec in self:
          if rec.garden == False:
              raise ValidationError('Garden Field is Empty')

    @api.model_create_multi
    def create(self,vals):
        res = super(Property, self).create(vals)
        print("CREATE Methode")
        return res

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        res = super(Property, self)._search(args, offset=0, limit=None, order=None, count=False, access_rights_uid=None)
        print("READ Methode")
        return res

    def write(self, vals):
        res = super(Property, self).write(vals)
        print("Update Methode")
        return res

    def unlink(self):
        res = super(Property, self).unlink()
        print("DELETE Methode")
        return res

    def set_to_draft(self):
        for rec in self:
            rec.status = "draft"

    def set_to_pending(self):
        for rec in self:
            rec.status = "pending"


    def set_to_sold(self):
        for rec in self:
            rec.status = "sold"

class PropertyLine(models.Model):
    _name = 'property.line'
    property_id = fields.Many2one("property")
    area = fields.Float()
    description = fields.Char()


