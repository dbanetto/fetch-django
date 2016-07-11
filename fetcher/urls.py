from django.conf.urls import url

from fetcher import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^status/$', views.status, name="status"),
    url(r'^log/$', views.log, name="log"),
    url(r'^force/fetch/$', views.force_fetch, name="force_fetch"),
    url(r'^force/sort/$', views.force_sort, name="force_sort"),
]
