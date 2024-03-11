from odoo import fields, models

class StationProperty(models.Model) :
    _name = 'station.property'
    _description = "Real time space station manager"
    name = fields.Char(required=True)
    description = fields.Text()
    entity = fields.Char()
    country = fields.Char()
    station_code = fields.Char()
    crew_size = fields.Integer(string = "Crew Size")
    launched_date = fields.Date()
    reentered_date = fields.Date()
    days_in_orbit = fields.Integer()
    days_occupied = fields.Integer()
    total_crew_and_visitor = fields.Integer()
    no_of_crew_visited = fields.Integer()
    no_of_robotic_visitor = fields.Integer()
    mass_at_launched = fields.Integer(string="Mass (lb)")
    astronauts_ids = fields.Many2many("station.astronauts", string = "Astronauts")
    pressurized_volume = fields.Integer(string="Pressurized Volumne (cu ft)")
    state = fields.Selection(
        string="Status",
        required=True,
        selection=[
            ("past_station", "Past Station"),
            ("prototypes", "Prototypes"),
            ("operational_stations", "Operational Stations"),
            ("planned_and_proposed", "Planned And Proposed"),
            ("cancelled_projects", "Cancelled Projects"),
        ],
        copy=False,
        default="prototypes",
    )
