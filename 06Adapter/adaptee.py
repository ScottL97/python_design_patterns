#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : adaptee.py
@Author: Scott
@Date  : 2022/2/6 12:37
@Desc  : 需要适配的之前写的类，使用新的接口能调用原来实现的功能
"""


class Adaptee:
    def __init__(self):
        self.name = "adaptee"

    def foo(self):
        print("foo", self.name)

    def bar(self):
        print("bar", self.name)
