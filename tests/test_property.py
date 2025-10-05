from odoo.tests.common import TransactionCase
from odoo import fields

class TestProperty(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestProperty, self).setUp()

        self.property_01_record = self.env['property'].create({
            'ref': 'PRT0001',
            'name': 'PROPERTY001',
            'description': '1000 PROPERTY',
            'postcode':'12365',
            'data_availability': fields.Date.today,
            'expected_selling_date': fields.Date.today,
            'is_late': fields.Float,
            'selling_price':1000,
            'expected_price': 1000,
            'diff': 1000,
            'bedrooms': 20,
            'living_area': 2,
            'facades': 30,
            'garage': 'T',
            'garden': 'F',
            'garden_area': 12,
            'garden_orientation':'north',

        })

    def test_01_property_values(self):
        property_id = self.property_01_record

        self.assertRecordValues(property_id,[{
            'ref': 'PRT0001',
            'name': 'PROPERTY001',
            'description': '1000 PROPERTY',
            'postcode': '12365',
            'data_availability': fields.Date.today,
            'expected_selling_date': fields.Date.today,
            'is_late': fields.Float,
            'selling_price': 1000,
            'expected_price': 1000,
            'diff': 1000,
            'bedrooms': 20,
            'living_area': 2,
            'facades': 30,
            'garage': 'T',
            'garden': 'F',
            'garden_area': 12,
            'garden_orientation': 'north',
        }])