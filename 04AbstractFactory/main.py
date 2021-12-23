#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: Scott
@Date  : 2021/12/9 0:28
@Desc  : 抽象工厂方法实现
"""
import pygame

from abstract_factory import CircleFactory, SquareFactory, draw_shape

if __name__ == '__main__':
    circle = CircleFactory()
    square = SquareFactory()

    if_quits = False

    while not if_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if_quits = True
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_s]:
                draw_shape(square)
            if pressed_key[pygame.K_c]:
                draw_shape(circle)
            pygame.display.flip()
