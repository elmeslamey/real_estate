from email.policy import default

from odoo import models, fields, api
from odoo.api import ValuesType, Self
from odoo.exceptions import ValidationError
from odoo.tools import Query
from odoo import models


class Building(models.Model):
    _name = 'building'
    _description = 'building Record'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'code'




    no = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    name = fields.Char()
    active = fields.Boolean(default=True)

