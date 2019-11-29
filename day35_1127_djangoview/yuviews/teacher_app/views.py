from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def teacher(r):
    return HttpResponse('这是一个teacher 视图')

def v2_exception(r):
    raise Http404
    return HttpResponse('OK')

def v10_1(r):
    return HttpResponseRedirect('/v11')

def v10_2(r):
    return HttpResponseRedirect(reverse('v11'))

def v11(r):
    return HttpResponse('哈哈，这是v11访问返回')

def v8_get(request):
    rst =''
    for k,v in request.GET.items():
        rst += k+'--->'+v
        rst +=','
    return HttpResponse('Get value of Request is {0}'.format(rst))

def v9_get(request):
    return render_to_response('for_post.html')
def v9_post(request):
    rst =''
    for k,v in request.POST.items():
        rst += k+'--->'+v
        rst +=','
    return HttpResponse('Get value of Request is {0}'.format(rst))
