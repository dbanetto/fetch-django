from django.conf.urls import patterns, url

from fetcher import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="index"),
    url(r'^status/$', views.status, name="status"),
    url(r'^force/fetch/$', views.force_fetch, name="force_fetch"),
    url(r'^force/sort/$', views.force_sort, name="force_sort"),
)
