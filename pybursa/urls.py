from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from pybursa.views import index, contact, students, student_detail, course_detail


urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^students/$', students, name='students'),
    url(r'^students/(?P<student_id>\d+)/$', student_detail, name='student_detail'),
    #url(r'^coaches/(?P<coach_id>\d+)/$', coach_detail, name='coach_detail'),
    #url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^courses/(?P<course_id>\d+)/$', course_detail, name='course_detail'),
    #url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
