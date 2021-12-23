#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : logger.py
@Author: Scott
@Date  : 2021/11/24 23:06
@Desc  : 
"""
import threading
import time


'''
def singleton2(cls):
    _instance = None

    def _singleton(*args, **kwargs):
        if _instance is None:  # 报错的可能原因是_instance还没有分配空间？
            _instance = cls(*args, **kwargs)
        return _instance

    return _singleton
'''


def singleton(cls):
    _instance = {}
    _instance_lock = threading.Lock()

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            with _instance_lock:
                if cls not in _instance:
                    _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton


@singleton
class Logger:
    def __init__(self, file_name, val):
        self.file_name = file_name
        self.val = val
        time.sleep(1)
