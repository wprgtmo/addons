from odoo import api, fields, models

class HCNurse(models.Model):
    _inherit = 'hr.employee'

    category_id = fields.Many2one(comodel_name='hc.nurse.category')

    certification_ids = fields.One2many(comodel_name='hc.nurse.certification', inverse_name='nurse_id')

    is_nurse=fields.Boolean()

    @api.onchange('is_nurse')
    def _onchange_is_nurse(self):
        jobs=self.env['hr.job'].search([('name','=','Nurse')])
        if jobs:
            job=jobs[0]
        else:
            job=self.env['hr.job'].create({'name': "Nurse"})        
        
        self.job_id= job.id



    

        

