from django.test import TestCase

from provider.models import BaseProvider, Provider
from provider.forms import base_provider_validator, ProviderForm


class ProviderFormTest(TestCase):
    fixtures = ['test_provider.json']

    @classmethod
    def setUp(cls):
        cls.base = BaseProvider.objects.all()[0]
        super(ProviderFormTest, cls).setUpClass()

    def test_base_provider_validator(self):
        self.assertEqual(False,
                         base_provider_validator(-1))
        self.assertEqual(True,
                         base_provider_validator(self.base.id))

    def test_from_provider(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com/",
            'regex_find_count': "\\d+",
            'base_provider_id': self.base.id,
        })
        self.assertEqual(True,
                         form.is_valid())
        form.full_clean()
        self.assertEqual("test",
                         form.cleaned_data['provider_name'])
        self.assertEqual("http://e.com/",
                         form.cleaned_data['provider_website'])
        self.assertEqual("\\d+",
                         form.cleaned_data['regex_find_count'])
        self.assertEqual(str(self.base.id),
                         form.cleaned_data['base_provider_id'])

    def test_all_filled_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider_id': self.base.id,
        })
        self.assertEqual(True,
                         form.is_valid())

    def test_name_not_valid(self):
        form = ProviderForm({
            'provider_name': "",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider_id': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())

    def test_website_not_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "",
            'regex_find_count': "\\d+",
            'base_provider_id': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "not a url",
            'regex_find_count': "\\d+",
            'base_provider_id': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())

    def test_regex_not_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "",
            'base_provider_id': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())

    def test_base_provider_id_not_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider_id': "",
        })
        self.assertEqual(False,
                         form.is_valid())
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider_id': -1,
        })
        self.assertEqual(False,
                         form.is_valid())

    def test_CHOICE_BASE_PROVIDERS(self):
        expected = ((self.base.id, self.base),)
        self.assertEqual(expected, ProviderForm.CHOICE_BASE_PROVIDERS)
