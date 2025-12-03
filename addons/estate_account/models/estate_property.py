from odoo import fields, models, api, Command
from datetime import timedelta
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateProperty(models.Model):

    _inherit = "estate.property"

    def action_mark_sold_button(self):
        print("🔥Action Mark Sold button() method override from estate_account module.")
        result = super(EstateProperty, self).action_mark_sold_button()
        invoice_values = {
            'partner_id':  self.buyer_id.id ,#the buyer
            'move_type': 'out_invoice',
            'invoice_line_ids': [
                Command.create({
                    'name': 'Commision Selling Price ',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06
                }),
                Command.create({
                    'name': 'Administrative Fees ',
                    'quantity': 1,
                    'price_unit': 100.00
                })
            ]
        }
        self.env['account.move'].create(invoice_values)

        return result