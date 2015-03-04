from django import forms
from django.core.validators import RegexValidator, URLValidator

from provider.models import BaseProvider


class ProviderForm(forms.Form):
    provider_name = forms.CharField(label='Provider Name')
    provider_website = forms.URLField(label="Webiste",
                                      validators=[URLValidator])

    base_provider = forms.ModelChoiceField(empty_label=None,
                                           queryset=BaseProvider.objects,
                                           label="Base Provider")
    regex_find_count = forms.CharField(max_length=256,
                                       label="Count Regex",
                                       validators=[RegexValidator])

    def from_provider(provider, initial=None):
        return ProviderForm({
            'provider_name': provider.name,
            'provider_website': provider.website,
            'regex_find_count': provider.regex_find_count,
            'base_provider': provider.base_provider.id,
        }, initial=initial)
