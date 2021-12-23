#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : profiling_decorator.py
@Author: Scott
@Date  : 2021/12/14 10:48
@Desc  : 用类和函数两种方法实现计算函数执行时间的装饰器
"""
import time
from functools import wraps


class ProfilingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print('with ProfilingDecorator:', self.func.__name__)
        print('ProfilingDecorator cost time:', end_time - start_time)

        return result


def profiling_decorator(f):
    @wraps(f)
    def wrap_f(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print('with profiling_decorator:', f.__name__)
        print('profiling_decorator cost time:', end_time - start_time)

        return result
    # 使用了wraps装饰器就不再需要这两句
    # wrap_f.__name__ = f.__name__
    # wrap_f.__doc__ = f.__doc__

    return wrap_f


def profiling_decorator_with_unit(unit):
    def _profiling_decorator(f):
        @wraps(f)
        def wrap_f(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            end_time = time.time()
            print('with profiling_decorator_with_unit:', f.__name__)
            if unit == "second":
                print('profiling_decorator_with_unit time:', (end_time - start_time) / 1000, "seconds")
            else:
                print('profiling_decorator_with_unit time:', end_time - start_time)

            return result

        return wrap_f
    return _profiling_decorator
