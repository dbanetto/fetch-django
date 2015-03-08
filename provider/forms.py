from django import forms
from django.core.validators import RegexValidator, URLValidator, ValidationError
from django.utils.translation import ugettext as _

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

    def clean(self):
        print(self)
        clean_data = super(ProviderForm, self).clean()
        options = {}
        for extra in clean_data['base_provider'].get_available_options():
            try:
                options[extra] = str(self.data['extra_options_' + extra])
                if options[extra] == "":
                    raise ValidationError(_('Invalid value: %(value)s '
                                            'cannot be null'),
                                          code='invalid',
                                          params={'value': str(extra)},
                                          )
            except KeyError:
                options[extra] = ""

        self.cleaned_data['options'] = options
