# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models
from odoo.exceptions import UserError


class Locations(models.Model):
    _name = 'aldaleel.location'

    QI_fSchoolName = fields.Char("English name")
    id1 = fields.Char()
    QI_ArabicName = fields.Char("Arabic name")
    QI_eSchoolID = fields.Char("School number")
    QII_6Latitude = fields.Char("Latitude")
    QII_5Longitude = fields.Char("Longitude")
    # price = fields.Float()
    # order_ids = fields.One2many("nursery.order", "plant_id", string="Orders")
    # order_count = fields.Integer(compute='_get_total_sold',
    #                              store=True,
    #                              string="Total sold")
    # number_in_stock = fields.Integer()

    # @api.depends('order_ids')
    # def _get_total_sold(self):
    #     for plant in self:
    #         plant.order_count = len(plant.order_ids)

    # @api.constrains('order_count', 'number_in_stock')
    # def _check_available_in_stock(self):
    #     for plant in self:
    #         if plant.number_in_stock and \
    #           plant.order_count > plant.number_in_stock:
    #             raise UserError("There is only %s %s in stock but %s were sold"
    #                   % (plant.number_in_stock, plant.name, plant.order_count))
