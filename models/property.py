

from odoo import models, fields, api
from odoo.api import ValuesType, Self
from odoo.exceptions import ValidationError
from odoo.tools import Query
import requests

class Property(models.Model):
    _name = 'property'
    _description = 'Property'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(default="NEW", readonly=1)
    name = fields.Char(required=1, default="NEW", size=20)
    description = fields.Text(tracking=1)
    postcode = fields.Char(required=1)
    data_availability = fields.Date(tracking=1)
    expected_selling_date = fields.Date(tracking=1)
    is_late = fields.Boolean()
    selling_price = fields.Float()
    expected_price = fields.Float()
    diff = fields.Float(compute='_compute_diff')
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
                                          default='North')
    owner_id = fields.Many2one("owner")
    tag_ids = fields.Many2many('tag')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
        ('closed', 'Closed'),
    ], default='draft')

    owner_address = fields.Char(related="owner_id.address", readonly=0)
    owner_phone = fields.Char(related="owner_id.phone", readonly=0)

    _sql_constraints = [
        ('unique_name', 'unique("name")', 'this name is exist!')
    ]

    line_ids = fields.One2many('property.line', 'property_id')

    active = fields.Boolean(default=True)

    @api.depends('expected_price', 'selling_price')
    def _compute_diff(self):
        for rec in self:
            rec.diff = rec.expected_price - rec.selling_price

    @api.constrains("bedrooms")
    def _check_bedroom_greater_zero(self):
        for rec in self:
            if rec.bedrooms == 0:
                raise ValidationError("please add valid number of bedrooms ")

    def action_draft(self):
        for rec in self:
            rec.create_history_record(rec.state, 'draft')
            rec.state = 'draft'

    def action_pending(self):
        for rec in self:
            rec.create_history_record(rec.state, 'pending')
            rec.write({
                'state': 'pending'
            })

    def action_sold(self):
        for rec in self:
            rec.create_history_record(rec.state, 'sold')
            rec.state = 'sold'

    def action_closed(self):
        for rec in self:
            rec.create_history_record(rec.state, 'closed')
            rec.state = 'closed'

    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late = True

    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     print('inside create method')
    #     return res
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None):
    #     res = super(Property, self)._search(domain, offset=0, limit=None, order=None)
    #     print('inside search method')
    #     return res
    #
    # def _write(self, vals):
    #     res = super(Property, self)._write(vals)
    #     print('inside write method')
    #     return res
    #
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print('inside unlink method')
    #     return res

    def action(self):
        print(self.env['owner'].search([]))

    @api.model
    def create(self, vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property_seq')
        return res



    def create_history_record(self, old_state, new_state ,reason):
        for rec in self:
            rec.env['property.history'].create({
                'user_id': rec.env.uid,
                'property_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or "",
            })

    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.change_state_wizard_action')
        action['context'] = {'default_property_id': self.id}
        return action


    def get_properties(self):
        payload = dict()
        try:
            response = requests.get('http://localhost:8018//v1/properties', data=payload)
            if response.status_code == 200:
                print('successful')
            else:
                print('fail')
        except Exception as error:
            raise ValidationError(str(error))




class PropertyLine(models.Model):
    _name = 'property.line'

    property_id = fields.Many2one('property')
    area = fields.Float()
    description = fields.Char()
