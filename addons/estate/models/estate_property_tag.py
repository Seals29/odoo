from odoo import fields, models
class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"
    _order = "name asc"

    name  = fields.Char(required=True)
    color= fields.Integer()

    _sql_constraints= [
        ('check_unique_estate_property_tag', 'UNIQUE(name)','Estate Property Tag must be Unique!!'),
    ]
