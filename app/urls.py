from django.conf.urls import include, url
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from app import views

base = r'^%s' % settings.URL_ROOT
urlpatterns = [
    re_path(base + r'admin/', admin.site.urls, name='admin'),
    re_path(base + r'provider/', include(('provider.urls', 'provider'))),
    re_path(base + r'series/', include(('series.urls', 'series'))),
    re_path(base + r'fetcher/', include(('fetcher.urls', "fetcher"))),

    re_path(base + r'$', views.index, name="index"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
