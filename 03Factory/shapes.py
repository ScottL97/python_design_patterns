#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : shapes.py
@Author: Scott
@Date  : 2021/12/8 23:53
@Desc  : 按下s键绘制正方形，按下c键绘制圆形
"""
from abc import ABCMeta, abstractmethod
import pygame

screen = pygame.display.set_mode((800, 600))


class Shape(metaclass=ABCMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
        pass

    @staticmethod
    def factory(shape_type):
        if shape_type == 'circle':
            return Circle(400, 300)
        elif shape_type == 'square':
            return Square(400, 300)
        print('ERROR', 'wrong shape type: ', shape_type)


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 100)


class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 100, 100))
