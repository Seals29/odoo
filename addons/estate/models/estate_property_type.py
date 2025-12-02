from odoo import fields, models
class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "name asc"

    name  = fields.Char(required=True)
    property_ids = fields.One2many("estate.property", "id", string="Property Ids")

    _sql_constraints= [
        ('check_unique_estate_property_type', 'UNIQUE(name)','Estate Property Type must be Unique!!'),
    ]