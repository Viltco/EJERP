# -*- coding: utf-8 -*-
from odoo import api, models


class ProductionReportInh(models.AbstractModel):
    _name = 'report.production_report.report_production_document'

    def get_variant_qty(self, product):
        model = self.env.context.get('active_model')
        rec_model = self.env[model].browse(self.env.context.get('active_id'))
        records = sum(self.env['sale.order.line'].search([('order_id.state', '=', 'sale'), ('product_id', '=', product.id)]).filtered(
            lambda t: t.order_id.date_order.date() == rec_model.date).mapped('product_uom_qty'))
        # print(records)
        return records

    def get_variant_bom(self, product):
        components_list = []
        dupl_list = []
        for bom in product.bom_ids:
            for line in bom.bom_line_ids:
                if line.product_id.id not in dupl_list:
                    components_list.append(line.id)
                    dupl_list.append(line.product_id.id)
        lines = self.env['mrp.bom.line'].browse(components_list)
        # print(lines)
        return lines

    def get_variant_bom_qty(self, bom, product):
        qty = 0
        # print(bom)
        for pro in product.product_variant_ids:
            sale = self.get_variant_qty(pro)
            # if bom.bom_id.product_id.id == pro.id:
            qty = qty + (sale * bom.product_qty)
                # qty = qty +
        # qty = 0
        # if bom.bom_id.product_id.id == product.id:
        #     qty = sale * bom.product_qty
        # for bom in product.bom_ids:
        #     pass
        # print(qty)
        return qty

    @api.model
    def _get_report_values(self, docids, data=None):
        model = self.env.context.get('active_model')
        rec_model = self.env[model].browse(self.env.context.get('active_id'))
        records = self.env['sale.order.line'].search([('order_id.state', '=', 'sale')]).filtered(lambda t: t.order_id.date_order.date() == rec_model.date)
        product_list = []
        for i in records:
            if i.product_id.product_tmpl_id.id not in product_list:
                product_list.append(i.product_id.product_tmpl_id.id)
        # partner_list = list(dict.fromkeys(partner_list))
        products = self.env['product.template'].browse(product_list)
        grad_lines = self.get_bom_lines(products)


        return {
            'doc_ids': self.ids,
            'doc_model': 'production_report.production.report.wizard',
            # 'partner_sales': self.get_partner_sales,
            'product_tmpls': products,
            'get_variant_qty': self.get_variant_qty,
            'get_variant_bom': self.get_variant_bom,
            'get_variant_bom_qty': self.get_variant_bom_qty,
            # 'qty': self.get_qty,
            'date': rec_model.date,
            'grad_lines': grad_lines,
            # 'date_to': rec_model.date_to.date(),
            # 'currency': currencies,
        }

    def get_bom_lines(self, products):
        bom_lines = []
        du_lines = []
        for product in products:
            for bom in product.bom_ids:
                for line in bom.bom_line_ids:
                    if line.product_id.id not in du_lines:
                        du_lines.append(line.product_id.id)
                        bom_lines.append(line.id)
        print(bom_lines)
        new_list = []
        for i in products:
            for j in bom_lines:
                bom = self.env['mrp.bom.line'].browse([j])
                qty = self.get_variant_bom_qty(bom, i)
                new_list.append({
                    'name': bom.product_id.name,
                    'qty': qty,
                    'uom': bom.product_uom_id.name,
                })
        print(new_list)
        return new_list


            # for variant in product.product_variant_ids:

