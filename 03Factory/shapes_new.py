#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : shapes_new.py
@Author: Scott
@Date  : 2022/2/2 15:13
@Desc  : 
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


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 100)


class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.x, self.y, 100, 100))


class ShapeFactory:
    @staticmethod
    def build(shape_type):
        if shape_type == 'circle':
            return Circle(400, 300)
        elif shape_type == 'square':
            return Square(400, 300)
        print('ERROR', 'wrong shape type: ', shape_type)
