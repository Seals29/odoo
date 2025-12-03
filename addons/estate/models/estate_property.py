from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    _order = "id desc"

    name  = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=lambda self: fields.Date.today(), copy=False)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Float()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ]
    )
    active = fields.Boolean(default=False)
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer received', 'Offer Received'),
            ('offer accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ],required=True, copy=False, default='new'
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    salesman_id = fields.Many2one("res.users", string="Salesman", index=True, default = lambda self: self.env.user, copy=True)
    buyer_id = fields.Many2one("res.partner", string="Buyer", index=True, copy=False)
    tag_ids = fields.Many2many("estate.property.tag", string="Property Tag")
    offer_ids = fields.One2many("estate.property.offer","property_id" ,string="Offer Ids")
    total_area = fields.Float(compute="_compute_total_area", string="Total Area (sqm)")
    best_price= fields.Float(compute="_compute_best_price", string="Best Offer")

    @api.onchange("garden")
    def _onchange_garden_area_orientation(self):
        if self.garden :
            self.garden_area = 10
            self.garden_orientation = "north"
            return 
            {
                'warning': 
                {
                    'title': _("Warning"),
                    'message': ('This option will enable garden Area (Default: 10) & Orientation (Default: North)')
                }    
            }
        else:
            self.garden = area = None
            self.garden_orientation = None


    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped("price"))
            else:
                record.best_price = 0.0

    def action_mark_sold_button(self):
        for record in self:
            if record.state == "canceled":
                raise UserError("Canceled property cannot be sold.")
            record.state = "sold"
        return True
    def action_mark_cancel_button(self):
        self.state = "canceled"
        return True
        
    @api.constrains('expected_price', 'selling_price')
    def _check_prices_positive(self):
        for record in self:
            if record.expected_price <= 0:
                raise ValidationError("Expected Price must be strictly positive")
            if record.selling_price and record.selling_price <= 0:
                raise ValidationError("Selling Price must be positive")

    @api.constrains("expected_price", "selling_price")
    def _check_selling_price(self):
        precision = 2
        for record in self:
            if not float_is_zero(record.selling_price, precision_digits=precision):
                if float_compare(record.selling_price, 0.9 * record.expected_price, precision_digits=precision) < 0:
                    raise ValidationError("Selling price cannot be lower than 90% of the expected price.")

    
            
    