import json

from django import forms
from django.core.validators import ValidationError
from django.utils.translation import ugettext as _

from series.models import MediaType, Series, poster_path
from provider.models import Provider
from app.validators import json_validator


class SeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = ['name',
                  'provider',
                  'media_type',
                  'poster',
                  'start_date',
                  'end_date',
                  'poster',
                  'current_count',
                  'total_count',
                  'release_schedule',
                  'media_type_options',
                  'release_schedule_options'
                  ]
        exclude = ()

    name = forms.CharField(label="Series Name")
    provider = forms.ModelChoiceField(queryset=Provider.objects,
                                      empty_label=None)
    media_type = forms.ModelChoiceField(queryset=MediaType.objects,
                                        empty_label=None)
    poster = forms.ImageField()
    start_date = forms.DateField()
    end_date = forms.DateField()

    release_schedule = forms.ChoiceField(choices=Series.RELEASE_SCHEDULE_CHOICES)

    current_count = forms.IntegerField(min_value=0)
    total_count = forms.IntegerField(min_value=0)

    media_type_options = forms.CharField(widget=forms.HiddenInput(),
                                         validators=[json_validator],
                                         required=False)
    release_schedule_options = forms.CharField(widget=forms.HiddenInput(),
                                               validators=[json_validator],
                                               required=False)

    def clean_options(self, key):
        options = self.cleaned_data[key]
        if type(options) is str:
            try:
                return json.loads(options)
            except ValueError as e:
                raise ValidationError(
                    _('Invalid JSON in %(owner)s : \"%(option)s\" '
                      '%(e)s '),
                    params={'e': e,
                            'owner': key,
                            'option': options}
                )
        elif type(options) is dict:
            return options
        else:
            raise ValidationError(
                _('Invalid input: Did not expect type %(type)s'),
                params={'type': type(options)})

    def clean_provider_options(self):
        return self.clean_options('provider_options')

    def clean_media_type_options(self):
        return self.clean_options('media_type_options')

    def clean(self):
        clean_data = super(SeriesForm, self).clean()
        if 'end_date' in clean_data and 'start_date' in clean_data:
            if clean_data['end_date'] != "" and \
               clean_data['start_date'] == "":  # TODO: Better error messages
                raise ValidationError(_('Invalid combination of Start Date and'
                                        ' End Date if End Date is not null then'
                                        ' Start Date must have a value'),
                                      code='invalid'
                                      )
            elif 'end_date' in clean_data and \
                 'start_date' not in clean_data:  # TODO: Better error messages
                raise ValidationError(_('Invalid combination of Start Date and'
                                        ' End Date if End Date is not null then'
                                        ' Start Date must have a value'),
                                      code='invalid'
                                      )
            if clean_data['start_date'] > clean_data['end_date']:
                msg = _('Invalid start and end dates start date must be before '
                        'the end')
                self.add_error('start_date', msg)
                self.add_error('end_date', msg)

        if 'total_count' in clean_data and 'current_count' in clean_data:
            if clean_data['total_count'] != 0 and \
               clean_data['current_count'] > clean_data['total_count']:
                msg = _('Must be lesser or equal to total count, '
                        'unless total count is zero')
                self.add_error('current_count', msg)
