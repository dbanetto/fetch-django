from django.conf.urls import patterns, url

from provider import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^(?P<provider_id>\d+)/$', views.view, name='view'),
    url(r'^(?P<provider_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<provider_id>\d+)/delete/$', views.delete, name='delete'),
)
