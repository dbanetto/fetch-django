import json

from django import forms
from django.core.validators import ValidationError
from django.utils.translation import ugettext as _

from provider.models import BaseProvider, Provider
from app.validators import json_validator


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
                                       label="Count Regex")

    options = forms.CharField(widget=forms.HiddenInput(),
                              validators=[json_validator])

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
