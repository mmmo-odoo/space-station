from odoo import fields, models

class StationProperty(models.Model) :
    _name = 'station.property'
    _description = "Real time space station manager"
    name = fields.Char(required=True)