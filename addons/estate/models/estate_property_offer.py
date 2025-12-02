from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price desc"

    price = fields.Float()
    status = fields.Selection(
        selection=[
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),

        ], copy=False
    )
    partner_id = fields.Many2one("res.partner", required=True)
    property_id = fields.Many2one("estate.property", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    property_state = fields.Selection(related="property_id.state", readonly=True)
    property_type_id = fields.Many2one(related="property_id.property_type_id", store=True)

    
    _sql_constraints= [
    ('check_offer_price_positive', 'CHECK(price IS NULL OR price > 0)', 'The offer price must be positive'),
       ]
    @api.depends("create_date","validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
               record.date_deadline = record.create_date + timedelta(days=record.validity) 
            else:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline and record.create_date:
                delta = record.date_deadline - record.create_date.date()
                record.validity = delta.days
            else:
                record.validity = (record.date_deadline - fields.Date.today()).days


    
    # @api.depends("offer_ids.status")
    def action_mark_accept_button(self):
        for record in self:
            if record.property_id.state == "sold":
                raise UserError("Cannot accept offer for a sold property")
            record.status = "accepted"
            record.property_id.state = "offer accepted"
            record.property_id.buyer_id = record.partner_id
            record.property_id.selling_price = record.price
            
        return True

    def action_mark_refuse_button(self):
        for record in self:
            record.status = "refused"
        return True


    @api.constrains('price')
    def _check_offer_prices_positive(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("Offer Price must be strictly positive")
    @api.model
    def create(self, vals):
        if 'property_id' in vals and 'price' in vals:
                existing_offers = self.env['estate.property.offer'].search([
                    ('property_id', '=', vals['property_id'])
                ])

                if existing_offers:
                    highest_price = max(existing_offers.mapped('price'))
                    if vals['price'] < highest_price:
                        raise ValidationError("Offer price must be higher than existing offers.")

            # Continue normal flow
        record = super().create(vals)
                
        if record.property_id:
            record.property_id.state = 'offer received'
        return record

  
