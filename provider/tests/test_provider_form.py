from django.test import TestCase

from provider.models import BaseProvider, Provider
from provider.forms import ProviderForm


class ProviderFormTest(TestCase):
    fixtures = ['test_provider.json']

    @classmethod
    def setUp(cls):
        cls.base = BaseProvider.objects.all()[0]

    def test_from_provider(self):
        p = Provider.objects.all()[0]
        form = ProviderForm.from_provider(p)
        self.assertEqual(True,
                         form.is_valid())
        form.full_clean()
        self.assertEqual(p.name,
                         form.cleaned_data['provider_name'])
        self.assertEqual(p.website,
                         form.cleaned_data['provider_website'])
        self.assertEqual(p.regex_find_count,
                         form.cleaned_data['regex_find_count'])
        self.assertEqual(p.base_provider,
                         form.cleaned_data['base_provider'])

    def test_all_filled_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
        })
        self.assertEqual(True,
                         form.is_valid())

    def test_name_not_valid(self):
        form = ProviderForm({
            'provider_name': "",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())

    def test_website_not_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "not a url",
            'regex_find_count': "\\d+",
            'base_provider': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())

    def test_regex_not_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "",
            'base_provider': self.base.id,
        })
        self.assertEqual(False,
                         form.is_valid())

    def test_base_provider_not_valid(self):
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': "",
        })
        self.assertEqual(False,
                         form.is_valid())
        form = ProviderForm({
            'provider_name': "test",
            'provider_website': "http://e.com",
            'regex_find_count': "\\d+",
            'base_provider': -1,
        })
        self.assertEqual(False,
                         form.is_valid())
