from django.conf.urls import patterns, url

from provider import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<provider_id>\d+)/$', views.view, name='view'),
)
