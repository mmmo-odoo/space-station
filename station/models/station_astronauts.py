from odoo import fields, models

class StationAstronauts(models.Model):
    _name = "station.astronauts"
    _description = "This Model is for only astronauts detail"
    name = fields.Char(required = True)
    date_of_birth = fields.Date()
    nationality = fields.Char()
    color = fields.Integer()
    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "female"),
            ("transgender", "Transgender")
        ],
        copy=False,
    )
    address = fields.Text()
    phone = fields.Char()
    email = fields.Char()
    bachlor = fields.Boolean()
    master = fields.Boolean()
    phd = fields.Boolean()
    medical_info = fields.Text()
    fitness_test = fields.Selection(
        selection=[
            ("passed", "Passed"),
            ("failed", "Failed"),
            ("not_attempted", "Not Attempted"),
        ],
        copy=False,
    )
    recent_medical_examination = fields.Selection(
        selection=[
            ("done", "Done"),
            ("not_done", "Not Done"),
            ("reamain", "Remain"),
        ],
        copy=False,
    )
    cardiovascular = fields.Boolean()
    muscular_health = fields.Boolean()

    bachlor_educational_institute = fields.Char()
    master_educational_institute = fields.Char()
    phd_educational_institute = fields.Char()
    work_experience = fields.Char()
    position = fields.Char()

