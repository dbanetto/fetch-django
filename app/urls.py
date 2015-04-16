from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from app import views

base = r'^%s' % settings.URL_ROOT
urlpatterns = patterns(
    '',
    url(base + r'admin/',
        include(admin.site.urls)),
    url(base + r'provider/',
        include('provider.urls', namespace='provider')),
    url(base + r'series/',
        include('series.urls', namespace='series')),
    url(base + r'fetcher/',
        include('fetcher.urls', namespace="fetcher")),

    url(base + r'$', views.index, name="index"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
