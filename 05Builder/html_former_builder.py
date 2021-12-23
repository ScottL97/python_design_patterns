#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : html_former_builder.py
@Author: Scott
@Date  : 2021/12/11 22:17
@Desc  : 实现生成HTML表单文件的Director和Builder
"""
from builder import Builder
from director import Director


class HTMLForm:
    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return "<form>{}</form>".format("".join(self.field_list))


class HTMLFormBuilder(Builder):
    def __init__(self):
        self.constructed_object = HTMLForm()

    def add_button_field(self, field_dict):
        self.constructed_object.field_list.append(
            '<button type="button">{}</button>'.format(
                field_dict["text"]
            )
        )

    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            '{0}:<br><input type="text" name="{1}"><br>'.format(
                field_dict["label"],
                field_dict["name"]
            )
        )


class HTMLFormDirector(Director):
    def __init__(self):
        Director.__init__(self)

    def set_builder(self, builder):
        self._builder = builder

    def construct(self, field_list):
        for field in field_list:
            field_type = field['field_type']
            if field_type == 'text':
                self._builder.add_text_field(field)
            elif field_type == 'button':
                self._builder.add_button_field(field)
