import json
from datetime import date, time
from urllib.request import urlopen, HTTPError

from django import forms
from django.core.validators import ValidationError
from django.utils.translation import ugettext as _
from django.utils import timezone
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from datetimewidget.widgets import DateWidget, TimeWidget

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
                  'current_count',
                  'total_count',
                  'release_schedule',
                  'media_type_options',
                  'release_schedule_options',
                  'release_time',
                  ]
        exclude = ()

    name = forms.CharField(label="Series Name")
    provider = forms.ModelChoiceField(queryset=Provider.objects,
                                      empty_label=None)
    media_type = forms.ModelChoiceField(queryset=MediaType.objects,
                                        empty_label=None)
    poster = forms.ImageField(required=False,
                              label="Upload Poster from local",
                              widget=forms.FileInput())
    poster_url = forms.URLField(required=False,
                                label="Upload Poster from URL")

    start_date = forms.DateField(initial=timezone.now().date(),
                                 required=False,
                                 widget=DateWidget(usel10n=True, bootstrap_version=3))
    end_date = forms.DateField(required=False,
                               widget=DateWidget(usel10n=True, bootstrap_version=3))

    release_time = forms.TimeField(initial=time(hour=12),
                                   required=False,
                                   widget=TimeWidget(bootstrap_version=3,
                                                     options={'format': 'hh:ii'}))
    release_schedule = forms.ChoiceField(choices=Series.RELEASE_SCHEDULE_CHOICES)

    current_count = forms.IntegerField(min_value=0,
                                       initial=0)
    total_count = forms.IntegerField(min_value=0,
                                     initial=0)

    media_type_options = forms.CharField(widget=forms.HiddenInput(),
                                         validators=[json_validator],
                                         initial="{}",
                                         required=False)
    release_schedule_options = forms.CharField(widget=forms.HiddenInput(),
                                               validators=[json_validator],
                                               initial="{}",
                                               required=False)

    def generate_release_schedule_options(self):
        return json.dumps({
            "N": [],
            "W": [],
            "F": [],
            "M": [],
            "D": ["dates"]
        })

    def clean_options(self, key):
        if key not in self.cleaned_data:
            return None

        options = self.cleaned_data[key]
        if type(options) is str:
            try:
                return json.loads(options)
            except ValueError as e:
                msg = _('Invalid JSON : ' + str(e))
                self.add_error(key, msg)
        elif type(options) is dict:
            return options
        elif type(options) is type(None):
            return None
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

        if 'end_date' in clean_data and clean_data['end_date'] is not None:
            if clean_data['start_date'] > clean_data['end_date']:
                msg = _('Invalid start and end dates start date must be '
                        'before the end')
                self.add_error('start_date', msg)
                self.add_error('end_date', msg)

        if 'total_count' in clean_data and 'current_count' in clean_data:
            if clean_data['total_count'] != 0 and \
               clean_data['current_count'] > clean_data['total_count']:
                msg = _('Must be lesser or equal to total count, '
                        'unless total count is zero')
                self.add_error('current_count', msg)

        if 'poster_url' in clean_data and 'poster' in clean_data:
            if clean_data['poster_url'] != "" and \
               (self.cleaned_data['poster'] is not None and
               self.cleaned_data['poster'] != self.instance.poster):
                msg = _('Cannot upload an image and a URL at the same time')
                self.add_error('poster', msg)
                self.add_error('poster_url', '')

        if self.instance is None and 'poster_url' not in clean_data and \
           'poster' not in clean_data:
            msg = _('Must have either an image to upload or url')
            self.add_error('poster', msg)
            self.add_error('poster_url', '')

        if 'poster_url' in self.cleaned_data and \
           self.cleaned_data['poster_url'] != "":
            url = self.cleaned_data['poster_url']
            if url.split('/')[-1].split('.')[-1] not in ['jpg', 'png', 'gif', 'jpeg']:
                msg = _('url must lead to an image of jpg, jpeg, png or gif format')
                self.add_error('poster', msg)
                self.add_error('poster_url', '')

        if 'poster_url' in self.cleaned_data and \
           self.cleaned_data['poster_url'] != "":
            url = self.cleaned_data['poster_url']
            if url.split('.')[-1] in ['jpg', 'png', 'gif', 'jpeg']:
                img_temp = NamedTemporaryFile(delete=True)
                try:
                    img_temp.write(urlopen(url).read())
                except HTTPError as e:
                    msg = _(str(e))
                    self.add_error('poster', msg)
                    self.add_error('poster_url', '')
                img_temp.flush()
                self.cleaned_data['poster_url_image'] = img_temp

    def save(self, *args, **kwargs):
        if 'poster_url_image' in self.cleaned_data:
            url = self.cleaned_data['poster_url']
            img_temp = self.cleaned_data['poster_url_image']
            self.instance.poster.save(poster_path(self.instance,
                                                  url.split('/')[-1]),
                                      File(img_temp))

        # TODO: Create thumbnail of poster

        return super(SeriesForm, self).save()
