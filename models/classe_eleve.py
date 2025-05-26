from odoo import _, api, fields, models, tools

class StudentClass(models.Model):

    _name = 'student.class'
    _description = 'Classe'

    name = fields.Char(string="Nom de classe")

    description = fields.Text(string="Description")

    student_ids = fields.One2many('school.student', 'class_id')

    student_count = fields.Integer(string="Total d'élèves", compute="_compute_student_count")

    def _get_student_count(self):
        self.student_count = len(self.student_ids)
    
    @api.depends('student_ids')
    def _compute_student_count(self):
        for record in self:
            record.student_count = len(record.student_ids)

    def student_list(self):
        return {
            'name':'Liste des élèves',
            'domain':[('class_id','=', self.id)],
            'res_model':'school.student',
            'view_id':False,
            'view_mode':'tree,form',
            'context':{'default_class_id': self.id},
            'type':'ir.actions.act_window',
        }

   

    
