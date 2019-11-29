from django.conf.urls import include, url
from django.contrib import admin
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^normalmap/',tv.do_normalmap),
    # #带参数url
    # url(r'withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),
    url(r'liudana/',views.do_app),
]

# 表明传符合正则，调用后面函数