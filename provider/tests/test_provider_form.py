from django.test import TestCase

from provider.models import BaseProvider
from provider.forms import ProviderForm


class ProviderFormTest(TestCase):
    fixtures = ['test_provider.json']

    @classmethod
    def setUp(cls):
        cls.base = BaseProvider.objects.all()[0]

    def test_all_filled_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{"id": "1"}',
        })
        self.assertTrue(form.is_valid())

    def test_name_not_valid(self):
        form = ProviderForm({
            'name': "",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid())

    def test_website_not_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid())
        form = ProviderForm({
            'name': "test",
            'website': "not a url",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid())

    def test_regex_not_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "",
            'base_provider': self.base.id,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid())

    def test_options_not_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\d+",
            'base_provider': self.base.id,
            'options': 'not json',
        })
        self.assertFalse(form.is_valid())
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\d+",
            'base_provider': self.base.id,
            'options': "10 things",
        })
        self.assertFalse(form.is_valid())

    def test_base_not_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': "",
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid())
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': -1,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid())

    def test_json_validation_insert_keys(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': "",
            'options': '{"hacking":"the gate"}',
        })
        self.assertFalse(form.is_valid())

    def test_json_validation_insert_keys_with_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': "",
            'options': '{"id":"1", "hacking":"the gate"}',
        })
        self.assertFalse(form.is_valid())

    def test_json_validation_leave_keys(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': "",
            'options': '{}',
        })
        self.assertFalse(form.is_valid())

    def test_regex_invalid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "*",
            'base_provider': "",
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid())
