# django_celery
celery实现异步的请求

首先安装celery    pip install celery

在django的项目路径下创建一个py文件
celery.py

#!/usr/bin/python
# -*- coding:utf-8 -*-
# project : CeleryTest
# user :taihe
# Author: 冀恩开
# createtime :2018/8/27 16:41

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CeleryTest.settings')

app = Celery('CeleryTest')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))















