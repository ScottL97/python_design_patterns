#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : adapter.py
@Author: Scott
@Date  : 2022/2/6 12:36
@Desc  : 通过对象适配器（通过组合而不是继承）实现适配器模式
"""


class Adapter:
    """
    Adapter类不需要继承需要适配的接口，是通过鸭子类型来去除继承性，Adapter实现接口所需的method_i_want方法即可认为实现了要适配的接口
    """
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def method_i_want(self):
        self.adaptee.foo()

    def __getattr__(self, attr):
        """
        我们只需要实现要适配的method_i_want方法，其他的方法都使用被适配的Adaptee类的方法
        """
        return getattr(self.adaptee, attr)
