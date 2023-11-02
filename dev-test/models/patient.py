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
    name = fields.Char(string="Name", required=True, tracking=True)
    
    # Computed Field for Capitalized Name. The Computed Field is an function trigger.
    # Like: <button onclick="onclick()"/>
    capitalized_name = fields.Char(string="Capitalized Name", tracking=True, readonly=True, computed="_compute_capitalized_name")

    # Field for the patient's birthdate (Date Type)
    birthday_date = fields.Date(string="Birthday Date", tracking=True)

    # Field for the patient's age (Integer type)
    age = fields.Integer(string="Age", tracking=True, readonly=True)

    # Field to indicate whether the patient is a child or not (Boolean type)
    is_child = fields.Boolean(string="Is Child?", tracking=True, readonly=True)

    # Field for adding textual notes or comments about the patient (Text type)
    notes = fields.Text(string="Notes", tracking=True)

    # Field for specifying the patient's gender, with a predefined selection of values
    gender = fields.Selection(
        string="Gender",
        selection=[('male', 'Male'), ('woman', 'Woman'), ('others', 'Others')],
        tracking=True
    )
    
    @api.depends('name')
    def _compute_capitalized_name(self):
        # Self need to be iterated
        # Because will contain every records
        for record in self:
            if record.name:
                record.capitalized_name = record.name.upper()
            else:
                record.capitalized_name = ''
    
    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False
            
    @api.onchange('birthday_date')
    def _onchange_birthday_date(self):  
        # Calculate age based on 'birthday_date'
        if self.birthday_date:
            # Calculate age based on the difference between the birthdate and the current date
            today = fields.Date.today()
            age = today.year - self.birthday_date.year - ((today.month, today.day) < (self.birthday_date.month, self.birthday_date.day))

            # Update the 'age' field with the calculated age
            self.age = age