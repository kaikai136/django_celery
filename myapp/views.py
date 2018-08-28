from celery.result import AsyncResult
from django.shortcuts import render,HttpResponse
import time
# Create your views here.
from myapp import tasks
def index(request):
    res = tasks.add.delay(5,98)
    print(res)
    return HttpResponse(res.task_id)

def task_res(request):
    result = AsyncResult(id='5fea266e-18ad-4659-aa8f-c5d16783defd')

    return HttpResponse(result.get())

