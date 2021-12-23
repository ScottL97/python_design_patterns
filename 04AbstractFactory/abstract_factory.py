#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : abstract_factory.py
@Author: Scott
@Date  : 2021/12/9 0:29
@Desc  : 
"""
from abc import ABCMeta, abstractmethod
from shapes import Circle, Square


class ShapeFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_obj(self):
        pass


class CircleFactory(ShapeFactory):
    def make_obj(self):
        return Circle()


class SquareFactory(ShapeFactory):
    def make_obj(self):
        return Square()


def draw_shape(shape):
    shape.make_obj().draw()
