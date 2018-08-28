#!/usr/bin/python
# -*- coding:utf-8 -*-
# project : CeleryTest
# user :taihe
# Author: 冀恩开
# createtime :2018/8/27 16:48

# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
#  @shared_task 所有试图都可以调用
@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)








