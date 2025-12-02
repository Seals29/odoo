from odoo import fields, models
class ResUsers(models.Model):
    _inherit = "res.users"

    # _name = "estate.property.tag"
    # _description = "Estate Property Tag"
    # _order = "name asc"

    property_ids = fields.One2many("estate.property", "salesperson_id", domain=[("state","in",["new", "offer received"])])
