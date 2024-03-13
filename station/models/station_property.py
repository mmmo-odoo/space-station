from odoo import fields, models

AVAILABLE_PRIORITIES = [
    ('0', 'Low'),
    ('1', 'Medium'),
    ('2', 'High'),
    ('3', 'Very High'),
]

class StationProperty(models.Model) :
    _name = 'station.property'
    _description = "Real time space station manager"
    name = fields.Char(required=True)
    description = fields.Text()
    entity = fields.Many2many("station.organization", string = "Organization")
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
    priority = fields.Selection(AVAILABLE_PRIORITIES, string='Priority', index=True,
        default=AVAILABLE_PRIORITIES[0][0])
    user_id = fields.Many2one('res.users', string='President', default=lambda self: self.env.user,
        domain="[('share', '=', False)]")
    module_ids = fields.One2many("station.modules", "station_ids")
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
    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')
