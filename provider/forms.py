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
            # Can assert will be valid json due to field validators
            value = json.loads(value)

        if type(value) is dict:
            # FIXME: needs alternative way to get base's schema for un-saved instances
            if 'base_provider' in self.cleaned_data:
                json_schema_check(value,
                                  self.cleaned_data['base_provider'].available_options)
            return value
        else:
            raise ValidationError(
                _('Invalid input: Did not expect type %(type)s'),
                params={'type': type(value)}
            )

    def clean(self):
        clean_data = super(ProviderForm, self).clean()
        return clean_data
