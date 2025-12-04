from odoo import _, api, fields, models
class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "name asc"

    name  = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Property Ids")
    sequence = fields.Integer()
    offer_ids = fields.One2many('estate.property.offer', 'property_type_id')
    offer_count = fields.Integer(compute="_compute_offer_count", string="Offer Count")

    _sql_constraints= [
        ('check_unique_estate_property_type', 'UNIQUE(name)','Estate Property Type must be Unique!!'),
    ]

    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)