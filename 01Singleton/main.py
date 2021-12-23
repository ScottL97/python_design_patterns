#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: Scott
@Date  : 2021/11/24 23:06
@Desc  : 使用python写一个完美的单例模式，注意以下几点
1、像日志类这样的类只需要在开始时将日志文件名等信息保存到类成员变量，后续一般不需要更改，不需要每次使用时创建一个对象，就适合使用单例模式
2、多个线程分别使用单例时，如果单例还没有创建，且单例类的构造函数__init__执行过慢，会导致最初的一段时间单例模式失效，要通过加锁判断单例
对象是否创建，但单例已经创建后，加锁会对性能产生损耗，所以可以进行优化，对单例是否创建进行二次判断，在获取锁前判断一次，TODO: 性能测试对比
3、TODO: 单例模式只有第一次构造函数的参数才有用，之后每次使用单例时传入的构造函数的参数都是没有意义的，而且很多时候并不需要传入参数，要解决这个问题
4、如果在类A中定义一个instance()类方法实现单例，就只能通过A.instance()获取单例，A()获取到的不是单例，容易造成用户误用
5、TODO: singleton2为什么报错，怎么解决这个问题
6、TODO: 对象执行构造函数前会执行__new__()方法，可以利用这一点实现单例，和当前通过装饰器的实现进行比较
"""
import threading
import time

from logger import Logger


def test1():
    """由于是单例模式，只有第一次才会创建对象"""
    l1 = Logger('l1.log', val=1)
    # 即使创建对象，构造函数传参也没有用到，因为还是取第一次创建的对象，不会新建对象
    l2 = Logger('l2.log', val=2)
    print(l1.val, l2.val)
    print(l1.file_name, l2.file_name)

    l1.val = 2
    l2.val = 3
    print(l1.val, l2.val)


def test2():
    """支持多线程"""
    def task(index):
        lo = Logger('%d.log' % index, index)
        print(index, lo)

    for i in range(10):
        t = threading.Thread(target=task, args=[i])
        t.start()

    time.sleep(2)


if __name__ == '__main__':
    test2()
