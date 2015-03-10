import json

from django import forms
from django.core.validators import ValidationError
from django.utils.translation import ugettext as _
from json_field import JSONField

from provider.models import BaseProvider
from app.validators import json_validator

class ProviderForm(forms.Form):
    provider_name = forms.CharField(label='Provider Name')
    provider_website = forms.URLField(label="Webiste")

    base_provider = forms.ModelChoiceField(empty_label="---",
                                           queryset=BaseProvider.objects,
                                           label="Base Provider")
    regex_find_count = forms.CharField(max_length=256,
                                       label="Count Regex")

    options = forms.CharField(widget=forms.HiddenInput(),
                              validators=[json_validator])

    def from_provider(provider, initial=None):
        return ProviderForm({
            'provider_name': provider.name,
            'provider_website': provider.website,
            'regex_find_count': provider.regex_find_count,
            'base_provider': provider.base_provider.id,
            'options': json.dumps(provider.options),
        }, initial=initial)

    def clean_options(self):
        clean_data = self.cleaned_data
        if type(clean_data['options']):
            try:

                return json.loads(clean_data['options'])
            except ValueError as e:
                raise ValidationError(
                    _('Invalid JSON'
                      '%(e)s'),
                    params={'e': e}
                )
        elif type(clean_data['options']) is dict:
            return clean_data['options']
        else:
            raise ValidationError(
                _('Invalid input: Did not expect type %(type)s'),
                params={'type': type(clean_data['options'])}
            )

    def clean(self):
        clean_data = super(ProviderForm, self).clean()
        # TODO: verify JSON is valid for the Base Provider
        return clean_data
