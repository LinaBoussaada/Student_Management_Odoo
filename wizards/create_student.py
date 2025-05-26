from odoo import _, api, fields, models, tools

class CreateStudent(models.TransientModel):

    _name = 'create.student'
    _description = 'Création d\'un élève'

    name = fields.Char(required=True)
    date = fields.Date()

    def create_student(self):
        vals={
            'name':self.name,
            'birth_date':self.date
        }
        student = self.env['school.student'].create(vals)
        return student