#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: Scott
@Date  : 2022/2/6 12:45
@Desc  : adaptee是以前写的类，adapter是适配了新接口的适配器，新接口要实现的方法调用了adaptee的方法，adaptee的其他方法可以通过adapter调用
"""
from adaptee import Adaptee
from adapter import Adapter


def new_interface_method(adapter):
    """
    新的接口需要实现method_i_want方法，即adapter要调用adaptee的方法来实现method_i_want方法
    """
    adapter.method_i_want()


if __name__ == '__main__':
    adaptee = Adaptee()
    my_adapter = Adapter(adaptee)
    new_interface_method(my_adapter)
    # adapter可以调用adaptee的方法
    my_adapter.bar()
