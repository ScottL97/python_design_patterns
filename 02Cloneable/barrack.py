#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : barrack.py
@Author: Scott
@Date  : 2021/12/7 23:15
@Desc  : RTS兵营，用于生成骑士等单位原型
"""
from rts_prototype import Knight


class Barrack:
    def __init__(self):
        self.cloneable_units = {
            'knight': {
                1: Knight(1),
                2: Knight(2)
            }
        }

    def build_unit(self, unit_type, level):
        return self.cloneable_units[unit_type][level].clone()
