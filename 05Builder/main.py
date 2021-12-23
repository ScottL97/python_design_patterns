#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : main.py
@Author: Scott
@Date  : 2021/12/11 23:55
@Desc  : 创建一个Director用来控制Builder生成表单，使用Builder创建各种类型的表单组件，问题：
1、TODO: field_list里的各键值使用时都未校验，可能导致崩溃，用户需要关心每种表单组件有哪些键值，怎么解决
2、TODO: 每次执行Director的get_constructed_object方法都要执行一次join，是否可以优化提升性能
3、TODO: HTMLFormBuilder的构造函数覆盖了Builder的，报Call to __init__ of super class is missed，怎么处理
"""
from html_former_builder import HTMLFormBuilder, HTMLFormDirector

if __name__ == '__main__':
    form_director = HTMLFormDirector()
    form_builder = HTMLFormBuilder()
    form_director.set_builder(form_builder)

    field_list = [
        {
            'field_type': 'text',
            'label': '用户名',
            'name': 'username'
        },
        {
            'field_type': 'button',
            'text': '提交'
        }
    ]

    form_director.construct(field_list)
    print(form_director.get_constructed_object())
    with open('test.html', 'w') as f:
        f.write('<html><head></head><body>{}</body></html>'.format(form_director.get_constructed_object()))
