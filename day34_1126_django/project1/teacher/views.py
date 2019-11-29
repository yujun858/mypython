from django.shortcuts import render
from django.http import HttpResponse
from django.


# Create your views here.
'''
视图函数需要一个参数，类型应该是HttpRequest
'''
def do_normalmap(request):
    # print('In do_normal')
    return HttpResponse('This is normalmap')

def withparam(request,year,month):
    return HttpResponse('This is with param {0},{1}'.format(year,month))

def do_app(request):
    return HttpResponse('子路由')

def do_param2(r,pn):
    return HttpResponse('page {0}'.format(pn))