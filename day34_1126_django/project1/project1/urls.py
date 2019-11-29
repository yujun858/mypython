from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/',tv.do_normalmap),
    #带参数url
    url(r'withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),
    # 比如约定，凡是teacher模块处理的视图url都是以teacher开头
    url(r'^teacher/',include(teacher_url)),
    #嵌套参数
    url(r'^book/(?:page-(?P<pn>\d+)/)$',tv.do_param2,name='reveParam')
]
# 表明传符合正则，调用后面函数