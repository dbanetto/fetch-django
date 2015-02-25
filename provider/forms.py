from django import forms
from django.core.validators import RegexValidator, URLValidator

from provider.models import BaseProvider


def base_provider_validator(value):
    try:
        BaseProvider.objects.get(pk=value)
        return True
    except:
        return False


class ProviderForm(forms.Form):
    provider_name = forms.CharField(label='Provider Name')
    provider_website = forms.URLField(label="Webiste",
                                      validators=[URLValidator])

    CHOICE_BASE_PROVIDERS = tuple((b.id, b)
                                  for b in BaseProvider.objects.all())
    base_provider_id = forms.ChoiceField(label="Base Provider",
                                         choices=CHOICE_BASE_PROVIDERS,
                                         validators=[base_provider_validator])
    regex_find_count = forms.CharField(max_length=256,
                                       label="Count Regex",
                                       validators=[RegexValidator])

    def base_provider(self):
        return BaseProvider.objects.get(
            pk=self.cleaned_data['base_provider_id'])

    def from_provider(provider):
        return ProviderForm({
            'provider_name': provider.name,
            'provider_website': provider.website,
            'regex_find_count': provider.regex_find_count,
            'base_provider_id': provider.base_provider.id,
        })
