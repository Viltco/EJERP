# -*- coding: utf-8 -*-

from odoo.exceptions import Warning
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    cust_note = fields.Char(string='Customer Note')
    f_name_bill = fields.Char(string='First Name Billing')
    l_name_bill = fields.Char(string='Last Name Billing')
    bill_address = fields.Char(string='Address Billing')
    bill_city = fields.Char(string='City Billing')
    bill_email = fields.Char(string='Email Billing')
    bill_phone = fields.Char(string='Phone Billing')
    f_name_ship = fields.Char(string='First Name Shipping')
    l_name_ship = fields.Char(string='Last Name Shipping')
    ship_address = fields.Char(string='Address Shipping')
    ship_city = fields.Char(string='City Shipping')
    con_code_ship = fields.Char(string='Country Code Shipping')
    ship_method = fields.Char(string='Shipping Method Title')
    pay_method = fields.Char(string='Payment Method Title')
    cart_disc = fields.Float(string='Cart Discount Amount')
    ship_order = fields.Float(string='Order Shipping Amount')
    refund_order = fields.Float(string='Order Refund Amount')
    product_id = fields.Char(string='Product Id')
    product_variation = fields.Char(string='Product Variation')
    coupon_code = fields.Char(string='Coupon Code')
    amount_disc = fields.Float(string='Discount Amount')
    disc_tax = fields.Float(string='Discount Amount Tax')
    delivery_time = fields.Char(string='Delivery Time')
    prod_type_2 = fields.Char(string='Product Type 2')
    order_date = fields.Date(string='Order Date')
    prod_type_text = fields.Char(string='Product Type Text')



