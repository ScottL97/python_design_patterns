#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: Scott
@Date  : 2021/12/8 23:49
@Desc  : 工厂方法实现，和原型模式不同的是，原型模式不需要子类化，需要初始化，工厂模式需要子类化，不需要初始化
1、当前窗口是shapes.py中的一个全局变量，在main.py里import的时候就会出现，非常不好，但如果在main.py里创建窗口，工厂方法就要把screen作为
参数传入，又不是标准的工厂方法的样子，TODO: 如何处理
2、TODO: 如果工厂要创建的产品数量很多，就要创建很多个工厂，有没有好的解决方法
3、Circle、Square都是工厂要创建的产品，用户理应不能自己创建它们，所以它们的构造方法应该为私有，但这里用户完全可以直接创建一个Square对象，
甚至可以调用Square.factory('square')，和Shape.factory('square')效果相同，TODO: 如何解决该问题
"""
import pygame

from shapes import Shape

if __name__ == '__main__':
    circle = Shape.factory('circle')
    square = Shape.factory('square')

    if_quits = False

    while not if_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if_quits = True
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_s]:
                square.draw()
            if pressed_key[pygame.K_c]:
                circle.draw()
            pygame.display.flip()
