#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: Scott
@Date  : 2021/12/7 22:54
@Desc  : 原型模式，思想：
1、创建一个抽象基类，指定一个纯虚方法clone()，要求它的子类必须实现该方法以满足原型模式要求，这里的clone()表示每个创建出的原型都是独立、互不干扰的；
2、在创建原型的类中，包含可以创建的原型的列表
3、TODO: 原型模式和工厂模式的不同：
4、RTS单位原型通过文件保存属性信息，构造函数中加载文件中的属性，之后只需要克隆而不需要每次创建一个原型都读取一次文件
5、TODO: RTS单位原型的构造函数中，如果属性多了，这样写会写很多行给对象的成员赋值，可扩展性不好，而且属性的数据类型不同，怎么处理
"""
from barrack import Barrack

if __name__ == '__main__':
    barrack = Barrack()
    knight1 = barrack.build_unit('knight', 1)
    knight2 = barrack.build_unit('knight', 2)

    print(knight1)
    print(knight2)
