from datetime import datetime, date
import json
from PIL import Image

from django.test import TestCase
from django.core.validators import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile

from series.forms import SeriesForm
from series.models import MediaType
from provider.models import Provider


class SeriesFromTest(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]

    def test_all_valid(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'poster_url': 'http://test.com/image.png',
            'start_date': datetime.now().date(),
            'end_date': None,
            'current_count': '0',
            'total_count': '0',
            'release_schedule': 'W',
            'media_type_options': '{}',
            'release_schedule_options': '{}',
            'release_time': datetime.now().time(),
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_all_minimal_valid(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/image.png',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_start_date_greater_than_end_date(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': date(2015, 1, 1),
            'end_date': date(2014, 1, 1),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/image.png',
        })
        self.assertFalse(form.is_valid())

        self.assertTrue('start_date' in form.errors)
        self.assertTrue('end_date' in form.errors)

    def test_start_date_less_than_end_date(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': date(2014, 1, 1),
            'end_date': date(2015, 1, 1),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/image.png',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_start_date_equal_end_date(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': date(2015, 1, 1),
            'end_date': date(2015, 1, 1),
            'current_count': '0',
            'total_count': '0',
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/image.png',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_no_total_count(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': '1',
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/image.png',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_total_current_count_equal(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': 1,
            'total_count': 1,
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/image.png',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_total_current_count_greater(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': 2,
            'total_count': 1,
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/image.png',
        })
        self.assertFalse(form.is_valid())
        self.assertTrue('current_count' in form.errors)

    def test_poster_url_invalid(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': 0,
            'total_count': 1,
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url' : "url"
        })
        self.assertFalse(form.is_valid())
        self.assertTrue('poster_url' in form.errors, form.errors)

    def test_poster_url_invalid_not_image(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': 0,
            'total_count': 1,
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url' : "http://url.com/file.txt"
        })
        self.assertFalse(form.is_valid())
        self.assertTrue('poster_url' in form.errors, form.errors)

    def test_poster_file(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        poster = SimpleUploadedFile("image.png", Image.new("1", (1,1)).tobitmap())
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': 0,
            'total_count': 1,
            'media_type_options': '{}',
            'release_schedule': 'W',
        }, {'poster': poster})
        self.assertTrue(form.is_valid(), form.errors)

    def test_poster_file_and_url(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        poster = SimpleUploadedFile("image.png", Image.new("1", (1,1)).tobitmap())
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': 0,
            'total_count': 1,
            'media_type_options': '{}',
            'release_schedule': 'W',
            'poster_url': 'http://test.com/'
        }, {'poster': poster})

        self.assertFalse(form.is_valid())

        self.assertTrue('poster' in form.errors, form.errors)
        self.assertTrue('poster_url' in form.errors, form.errors)

    def test_niether_poster_file_or_url(self):
        prov = Provider.objects.all()[0]
        media = MediaType.objects.all()[0]
        form = SeriesForm({
            'title': 'test',
            'search_title': 'test',
            'provider': prov.id,
            'media_type': media.id,
            'start_date': datetime.now().date(),
            'current_count': 0,
            'total_count': 1,
            'media_type_options': '{}',
            'release_schedule': 'W',
        })

        self.assertFalse(form.is_valid())

        self.assertTrue('poster' in form.errors, form.errors)
        self.assertTrue('poster_url' in form.errors, form.errors)

    def test_clean_options_valid(self):
        form = SeriesForm()
        form.cleaned_data = {'TEST': '{}'}
        self.assertEquals(form.clean_options("TEST"), {})

    def test_options_key_not_existing(self):
        form = SeriesForm()
        form.cleaned_data = {'TEST': '{}'}
        self.assertEquals(form.clean_options("NONE"), None)

    def test_clean_options_invalid_json(self):
        # Note using an actual field to check errors
        form = SeriesForm()
        form.cleaned_data = {'title': '{]'}
        self.assertEquals(form.clean_options("title"), None)
        self.assertTrue('title' in form.errors)

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

    def test_release_schedule_options(self):
        self.assertEquals(SeriesForm().generate_release_schedule_options(),
                          json.dumps({"N": [],"W": [], "F": [], "M": [], "D": ["dates"]}))
