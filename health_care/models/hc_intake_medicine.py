from odoo import api, fields, models

class HCIntakeMedicine(models.Model):
    _name = 'hc.intake.medicine'
    _description = 'HC Intake Medicine'

    intake_id = fields.Many2one(comodel_name='hc.intake')
    medicine_id = fields.Many2one(comodel_name='hc.medicine')
    
    frequency = fields.Char()
    dose = fields.Char()
    observation = fields.Text()




