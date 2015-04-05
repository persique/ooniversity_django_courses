from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^results/(?P<a>\d+)/(?P<b>\d+)/(?P<c>\d+)/$', views.results, name='results'),
)
