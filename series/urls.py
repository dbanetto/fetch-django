from django.conf.urls import patterns, url

from series import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<series_id>\d+)/$', views.view, name='view'),
    url(r'^(?P<series_id>\d+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<series_id>\d+)/delete/$', views.delete, name='delete'),
)
