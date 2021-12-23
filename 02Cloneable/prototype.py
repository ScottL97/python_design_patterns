#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : prototype.py
@Author: Scott
@Date  : 2021/12/7 23:00
@Desc  : 原型模式的抽象基类
"""
from abc import ABCMeta, abstractmethod


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass
