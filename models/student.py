from odoo import _, api, fields, models, tools
from datetime import date
from datetime import datetime

class SchoolStudent(models.Model):

    _name = 'school.student'  # Correction ici
    _inherit= ['mail.thread','mail.activity.mixin']
    _description = 'Student'
    email = fields.Char(tracking=False)  # Désactive le suivi des modifications
    
    
    matricule = fields.Char(string="Matricule", readonly=True)
    name = fields.Char(string='Nom de famille' , 
    track_visibility='onchange')

    birth_date = fields.Date(string='Date de naissance', default=date.today(), 
    track_visibility='onchange')
   # description = fields.Text(string='Description')
    photo = fields.Binary(string="Photo")
    description = fields.Html()
    is_former_student = fields.Boolean(string="Est ancien élève")
    sexe = fields.Selection(
        selection=[
            ('Masculin', 'Masculin'),
            ('Féminin', 'Féminin'),
            ('Autre', 'Autre'),
        ],
        string="Sexe",
        required=True,
        default='Féminin',
        store=True
    )
    age = fields.Integer(string="Age", track_visibility='onchange', compute="_compute_age")
    note = fields.Float(string="Note")

    class_id = fields.Many2one(
        'student.class',
        string='Classe',
    )
    date_start = fields.Datetime(string="Date et heure de début", default=datetime.now())
    course_ids = fields.Many2many('school.course', string="Cours")
    
    note_ids = fields.One2many('student.note', 'student_id')

    
    phone = fields.Char(string="Téléphone", 
    track_visibility='onchange', default="92416645"
    )

    progression = fields.Float(string="Progression", default=23)
    course_time = fields.Float(string="Heure de cours")

    priority = fields.Selection([
        ('moyen', 'Moyen'),
        ('normal','Norml'),
        ('eleve','Elevé'),
        ('Tres eleve','Très elevé')
    ], default="eleve")

    state = fields.Selection([
        ('inscription', 'Inscription'),
        ('abandonne', 'Abandonné'),
        ('exclu', 'Exclu'),
        ('preinscription', 'Préinscription'),
    ], default='preinscription', string="State")

    color = fields.Char(string="Couleur")

    other_color = fields.Integer(string="Autre couleur")

    active = fields.Boolean(default=True)


    @api.model
    def create(self, values):
        values['matricule'] = self.env['ir.sequence'].next_by_code('school.student')

        result = super().create(values)
        
        return result
    def _compute_age(self):
        for eleve in self:
            age = 0
            if eleve.birth_date:
                today = date.today()
                birth_date = eleve.birth_date
                age = today.year - birth_date.year
            eleve.age = age
    def compute_preinscription(self):
        for eleve in self:
            print('toto')
            eleve.state = 'preinscription'

    def compute_excul(self):
        for eleve in self:
            eleve.state = 'exclu'

    def compute_abandonne(self):
        for eleve in self:
            eleve.state = 'abandonne'

    def compute_inscription(self):
        for eleve in self:
            eleve.state = 'inscription'

    def compute_progress(self):
        self.progression +=  5
    
    def is_button_visible(self, button_name):
        if button_name == 'inscription':
            return self.state not in ['inscription', 'abandonne', 'exclu']
        elif button_name == 'abandonne':
            return self.state not in ['exclu', 'abandonne']
        elif button_name == 'exclu':
            return self.state not in ['exclu', 'inscription']
        elif button_name == 'preinscription':
            return self.state != 'exclu'
        return False