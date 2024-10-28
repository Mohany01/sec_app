from email.policy import default

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(required=1, default='New',track_visibility='always')
    description = fields.Text(track_visibility='always')
    postcode = fields.Char(required=1, size=4,track_visibility='always')
    date_availability = fields.Date(track_visibility='always')
    expected_price = fields.Float(track_visibility='always')
    selling_price = fields.Float(track_visibility='always')
    diff = fields.Float(compute='_compute_diff', store=1,track_visibility='always')
    bedrooms = fields.Integer(size=1, track_visibility='always')
    living_area = fields.Integer(size=1, track_visibility='always')
    facades = fields.Integer(track_visibility='always')
    garage = fields.Boolean(track_visibility='always')
    garden = fields.Boolean(track_visibility='always')
    garden_area = fields.Integer(size=3,track_visibility='always')
    owner_id = fields.Many2one("owner", required=1,track_visibility='always')
    tag_ids = fields.Many2many("tag",track_visibility='always')
    line_ids = fields.One2many("property.line", "property_id",track_visibility='always')
    owner_phone = fields.Char(related='owner_id.phone',track_visibility='always')
    owner_address = fields.Char(related='owner_id.address',track_visibility='always')
    active = fields.Boolean(default=True)

    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('west', 'West'),
        ('east', 'East'),
    ])
    status = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed')
    ] ,default="draft",track_visibility='always')
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

    def set_to_closed(self):
        for rec in self:
            rec.status = "closed"

class PropertyLine(models.Model):
    _name = 'property.line'
    property_id = fields.Many2one("property")
    area = fields.Float()
    description = fields.Char()


