#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : director.py
@Author: Scott
@Date  : 2021/12/11 22:21
@Desc  : 实现Director的抽象基类
"""
from abc import ABCMeta, abstractmethod


class Director(metaclass=ABCMeta):
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self, filed_list):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object
