#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : builder.py
@Author: Scott
@Date  : 2021/12/11 22:17
@Desc  : 实现Builder的抽象基类
"""
from abc import ABCMeta, abstractmethod


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_button_field(self, field_dict):
        pass
