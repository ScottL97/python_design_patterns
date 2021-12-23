#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : shapes.py
@Author: Scott
@Date  : 2021/12/9 0:34
@Desc  : 
"""
from abc import ABCMeta, abstractmethod
import pygame

screen = pygame.display.set_mode((800, 600))


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (255, 255, 0), (400, 300), 100)


class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(400, 300, 100, 100))