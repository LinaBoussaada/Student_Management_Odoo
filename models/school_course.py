from odoo import _, api, fields, models, tools

class SchoolCourse(models.Model):

    _name = 'school.course'
    _description = 'Cours'

    name = fields.Char(string="Nom du cours")
    