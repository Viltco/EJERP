from odoo import models, fields, api,_
from odoo.exceptions import UserError


class ProductionReportWizard(models.TransientModel):
    _name = 'production.report.wizard'

    date = fields.Date('Date')
    # product_ids = fields.Many2many('product.product')

    def print_report(self):
        data = {}
        data['form'] = self.read(['date'])[0]
        return self.env.ref('production_report.action_production_pdf_report').report_action(self, data=data, config=False)
