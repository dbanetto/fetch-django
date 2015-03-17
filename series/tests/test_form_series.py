from datetime import datetime, date

from django.test import TestCase
from django.core.validators import ValidationError

from series.forms import SeriesForm
from series.models import MediaType
from provider.models import Provider

class SeriesFromTest(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]

    def test_all_valid(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'name': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'poster': None,
            'start_date': datetime.now().date(),
            'end_date': None,
            'current_count': '0',
            'total_count': '0',
            'release_schedule': 'W',
            'media_type_options': '{}',
            'release_schedule_options': '{}',
            'release_time': datetime.now().time(),
        })
        self.assertTrue(form.is_valid())

    def test_all_minimal_valid(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'name': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
        })
        self.assertTrue(form.is_valid(), str(form.errors))

    def test_start_date_greater_than_end_date(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'name': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': date(2015, 1, 1),
            'end_date': date(2014, 1 ,1),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
        })
        self.assertFalse(form.is_valid())

    def test_start_date_less_than_end_date(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'name': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': date(2014, 1, 1),
            'end_date': date(2015, 1 ,1),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
        })
        self.assertTrue(form.is_valid())

    def test_start_date_equal_end_date(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'name': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': date(2015, 1, 1),
            'end_date': date(2015, 1 ,1),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
        })
        self.assertTrue(form.is_valid())

    def test_clean_options_valid(self):
        form = SeriesForm()
        form.cleaned_data = {'TEST': '{}'}
        self.assertEquals(form.clean_options("TEST"), {})

    def test_clean_options_invalid_json(self):
        # Note using an actual field to check errors
        form = SeriesForm()
        form.cleaned_data = {'name': '{]'}
        self.assertEquals(form.clean_options("name"), None)
        self.assertTrue('name' in form.errors)

    def test_clean_options_none(self):
        form = SeriesForm()
        form.cleaned_data = {'TEST': None}
        self.assertEquals(form.clean_options("TEST"), None)

    def test_clean_options_dict_type(self):
        form = SeriesForm()
        form.cleaned_data = {'TEST': {'a': 1}}
        self.assertEquals(form.clean_options("TEST"), {'a': 1})

    def test_clean_options_wrong_type(self):
        form = SeriesForm()
        form.cleaned_data = {'TEST': 1}
        with self.assertRaises(ValidationError):
            form.clean_options("TEST")

