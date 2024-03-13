from odoo import fields, models

class StationModules(models.Model):
    _name = "station.modules"
    _description = "shows station modules"
    name = fields.Char(required = True)
    description = fields.Text()
    type = fields.Char()
    launch_date = fields.Date()
    manufacturer = fields.Many2one("res.partner", string = "Manufacturer")
    dimension = fields.Integer()
    length = fields.Integer()
    width = fields.Integer()
    height = fields.Integer()
    mass = fields.Integer()
    # installed_quipment = fields.Many2one("product.product", string = "Equipments")
    # there will be one  relation with module and all product associated
    station_ids = fields.Many2one("station.property")
    status = fields.Selection(
        string="Status",
        required=True,
        selection=[
            ("operational", "Operational"),
            ("under_maintenance", "Under Maintenance"),
            ("decommissioned", "Decommissioned"),
        ],
        copy=False,
        default="operational",
    )
    stage = fields.Selection(
        string="Stage",
        required=True,
        selection=[
            ("conceptual_design", "Conceptual Design"),
            ("detailed_design", "Detailed Design"),
            ("fabrication_of_component", "Fabrication Of Component"),
            ("assembly", "Assembly"),
            ("integration", "Integeration"),
            ("testing", "Testing"),
            ("verification_and_validation", "Verification And Validation"),
            ("delivery_and_launch_preperation", "Delivery & Launch"),
            ("launch", "Launch"),
            ("done", "Done"),
        ],
        copy=False,
        default="conceptual_design",
    )
    mission_history = fields.Text()
    crew_capacity = fields.Integer()
    life_expectation = fields.Integer()
    maintenance_record = fields.Text()
    upcoming_maintenace_schedule = fields.Date()
    power_requirement = fields.Integer()
    notes = fields.Text()