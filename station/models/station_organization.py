from odoo import fields, models

class StationOgranization(models.Model):
    _name = "station.organization"
    _description = "It shows the different organization which involves in station management"
    name = fields.Char()
    sequence = fields.Integer()
    color = fields.Integer()
