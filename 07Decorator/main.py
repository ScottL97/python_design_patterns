#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: Scott
@Date  : 2021/12/14 10:50
@Desc  : 使用装饰器类/函数计算费波纳茨函数的执行时间，思想：
1、闭包就是让一个函数返回另一个定义在其内的函数，并且这个定义在其内的函数要引用位于容器函数范围内的变量，当容器函数退出时从命名空间移除的原始变量
会被存储在闭包函数中
2、python中一切皆对象，函数是定义了__call__方法的对象，所以可以用定义了__call__方法的对象或者函数作为装饰器
3、理想情况我们不希望以任何方式修改使用装饰器的任何函数，所以还需要修改__name__和__doc__属性为被装饰函数的属性，python内置了wraps装饰器可以
实现将被装饰的函数的__name__和__doc__属性赋值给装饰器函数内部的闭包函数，注意要用wraps装饰的是装饰器内部的装饰器函数，参数为被装饰函数
4、一个函数可以使用多个装饰器，但该函数只会被调用一次，TODO: 两个装饰器的执行顺序是什么
5、如果需要装饰一个类中的多个方法，可以在每个方法前面加装饰器，但违背了DRY（Don't Repeat Yourself）原则
"""
from profiling_decorator import profiling_decorator, ProfilingDecorator, profiling_decorator_with_unit


@ProfilingDecorator
@profiling_decorator
@profiling_decorator_with_unit("second")
def fib(n):
    if n < 2:
        return

    prev, current = 1, 1
    for num in range(2, n):
        prev, current = current, prev + current

    return current


if __name__ == '__main__':
    print(fib(10000))
