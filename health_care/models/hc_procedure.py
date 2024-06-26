from odoo import _, api, fields, models


class HCProcedure(models.Model):
    _name = 'hc.procedure'
    _description = 'HC Procedure'

    name = fields.Char()
    code = fields.Char()
    description = fields.Text()
    supply_ids = fields.Many2many(comodel_name='hc.supply')
