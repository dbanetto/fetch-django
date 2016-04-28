from django.test import TestCase
from django.core.validators import ValidationError

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
        self.assertTrue(form.is_valid(), form.errors)

    def test_name_not_valid(self):
        form = ProviderForm({
            'name': "",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_website_not_valid(self):
        for site in ["", "not url"]:
            with self.subTest(site=site):
                form = ProviderForm({
                    'name': "test",
                    'website': site,
                    'regex_find_count': "\\d+",
                    'base_provider': self.base.id,
                    'options': '{"id":"1"}',
                })
                self.assertFalse(form.is_valid(), form.errors)

    def test_regex_not_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "",
            'base_provider': self.base.id,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_options_not_valid_json(self):
        for bad_json in ['not json', '10 things']:
            with self.subTest(bad_json=bad_json):
                form = ProviderForm({
                    'name': "test",
                    'website': "http://e.com",
                    'regex_find_count': "\d+",
                    'base_provider': self.base.id,
                    'options': bad_json,
                })
                self.assertFalse(form.is_valid(), form.errors)

    def test_base_not_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': -1,
            'options': '{"id":"1"}',
        })
        with self.assertRaises(Exception):
            form.is_valid()

    def test_json_validation_insert_keys(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{"hacking":"the gate"}',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_json_validation_insert_keys_with_valid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{"id":"1", "hacking":"the gate"}',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_json_validation_leave_keys(self):
        self.base.available_options = {
            "properties": {"id": {"type": "string"},
                           "n": {"type": "string"}},
            "required": ["n"]
        }
        self.base.save()

        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '{}',
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_regex_invalid(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "*",
            'base_provider': self.base.id,
            'options': '{"id":"1"}',
        })
        self.assertFalse(form.is_valid(), form.errors)

    def test_options_invalid_type(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "r",
            'base_provider': self.base.id,
            'options': 1,
        })

        self.assertFalse(form.is_valid(), form.errors)
        self.assertTrue('options' in form.errors, form.errors)

    def test_empty_options(self):
        form = ProviderForm({
            'name': "test",
            'website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
            'options': '',
        })
        self.assertTrue(form.is_valid(), form.errors)
        self.assertEqual(form.clean_options(), {})
