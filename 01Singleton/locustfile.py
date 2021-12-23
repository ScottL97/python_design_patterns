#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File  : locustfile.py
@Author: Scott
@Date  : 2021/11/25 0:09
@Desc  : 
"""
from locust import HttpUser, TaskSet, task, between
from logger import Logger


class MyTasks(TaskSet):
    @task
    def task1(self):
        lo = Logger('test.log', 10)
        print(lo)


class RunTasks(HttpUser):
    tasks = [MyTasks]
    min_wait = 100
    max_wait = 500
