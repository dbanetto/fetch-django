from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from app import views

base = settings.URL_ROOT
urlpatterns = [
    url(r'^admin/',
        include(admin.site.urls), prefix=base),
    url(r'^provider/',
        include('provider.urls', namespace='provider'), prefix=base),
    url(r'^series/',
        include('series.urls', namespace='series'), prefix=base),
    url(r'^fetcher/', include('fetcher.urls', namespace="fetcher"), prefix=base),

    url(base + r'$', views.index, name="index", prefix=base),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
