import json

from django import forms
from django.core.validators import ValidationError
from django.utils.translation import ugettext as _

from provider.models import BaseProvider, Provider
from app.validators import json_validator, regex_validator, json_schema_check


class ProviderForm(forms.ModelForm):

    class Meta:
        model = Provider
        fields = ['name',
                  'website',
                  'base_provider',
                  'regex_find_count',
                  'options']
        exclude = ()

    name = forms.CharField(label='Provider Name')
    website = forms.URLField(label="Webiste")

    base_provider = forms.ModelChoiceField(empty_label=None,
                                           queryset=BaseProvider.objects,
                                           label="Base Provider")
    regex_find_count = forms.CharField(max_length=256,
                                       label="Count Regex",
                                       validators=[regex_validator])

    options = forms.CharField(widget=forms.HiddenInput(),
                              validators=[json_validator])

    def clean_options(self):
        value = self.cleaned_data['options']
        if type(value) is str:
            try:
                return json.loads(value)
            except ValueError as e:
                raise ValidationError(
                    _('Invalid JSON'
                      '%(e)s'),
                    params={'e': e}
                )
        elif type(value) is dict:
            return value
        else:
            raise ValidationError(
                _('Invalid input: Did not expect type %(type)s'),
                params={'type': type(value)}
            )

    def clean(self):
        clean_data = super(ProviderForm, self).clean()
        # TODO: verify JSON is valid for the Base Provider
        if 'options' in clean_data and 'base_provider' in clean_data:
            json_schema_check(clean_data['options'],
                              clean_data['base_provider'].get_available_options())
        return clean_data
