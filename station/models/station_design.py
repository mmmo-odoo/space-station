from odoo import fields , models

class StationDesign(models.Model):
    _name = "station.design"
    _description = "design of station"
    name = fields.name(required = True)
    image_1920 = fields.Image(
        "Image", 
        related='employee_id.image_1920', 
        compute_sudo=True
    )