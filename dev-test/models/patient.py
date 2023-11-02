# Import necessary modules from Odoo
from odoo import api, fields, models

# Define a custom Odoo model named "HospitalPatient"
class HospitalPatient(models.Model):
    # Specify the technical name of the model, which will be used as the database table name
    _name = "hospital.patient" # The Odoo will replace "." by "_" in database and will be "hospital.patient" to "hospital_patient"
    
    # Inherit mail_thread fields for "Chatter" funcionality (For Tracking Changes)
    _inherit = ['mail.thread']

    # Provide a description for the model, which will be displayed in Odoo's "Settings / Technical / Database Structure / Models"
    _description = "Patient Records"

    # Define fields for the "HospitalPatient" model
    # Each field represents a piece of information about a patient

    # Field for the patient's name, a required field (Char means character/string)
    name = fields.Char(string="Name", required=True)

    # Field for the patient's birthdate (Date Type)
    birthday_date = fields.Date(string="Birthday Date")

    # Field for the patient's age (Integer type)
    age = fields.Integer(string="Age")

    # Field to indicate whether the patient is a child or not (Boolean type)
    is_child = fields.Boolean(string="Is Child?")

    # Field for adding textual notes or comments about the patient (Text type)
    notes = fields.Text(string="Notes")

    # Field for specifying the patient's gender, with a predefined selection of values
    gender = fields.Selection(
        string="Gender",
        selection=[('male', 'Male'), ('woman', 'Woman'), ('others', 'Others')]
    )
