from django.contrib import admin

from provider.models import Provider, BaseProvider


admin.site.register(Provider)
admin.site.register(BaseProvider)
