#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : rts_prototype.py
@Author: Scott
@Date  : 2021/12/7 23:01
@Desc  : RTS游戏单位的原型，继承原型抽象基类，实现clone()方法深拷贝自身
"""
from prototype import Prototype
from copy import deepcopy


class Knight(Prototype):
    def __init__(self, level):
        self.unit_type = 'knight'

        data_file = '{}_{}.dat'.format(self.unit_type, level)
        with open(data_file, 'r') as f:
            for line in f.readlines():
                key_value = line.split('=')
                if len(key_value) != 2:
                    continue
                if key_value[0] == 'life':
                    self.life = int(key_value[1])
                elif key_value[0] == 'speed':
                    self.speed = int(key_value[1])
                elif key_value[0] == 'attack power':
                    self.attack_power = int(key_value[1])
                elif key_value[0] == 'attack range':
                    self.attack_range = int(key_value[1])
                elif key_value[0] == 'weapon':
                    self.weapon = key_value[1]

    def __str__(self):
        return 'unit type: {}\n' \
               'life: {}\n' \
               'speed: {}\n' \
               'attack power: {}\n' \
               'attack range: {}\n' \
               'weapon: {}'.format(self.unit_type, self.life, self.speed, self.attack_power, self.attack_range,
                                   self.weapon)

    def clone(self):
        return deepcopy(self)
