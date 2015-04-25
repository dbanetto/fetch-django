import json

from django.test import TestCase
from django.core.validators import ValidationError

from provider.models import Provider


class ProviderMethodTests(TestCase):
    fixtures = ['test_provider.json']

    def test_base_provider_options(self):
        p = Provider.objects.all()[0]
        p.options = {"test": "value"}
        self.assertEquals(p.base_provider_options_json(),
                          '{"test": "value"}')

    def test_name_empty(self):
        p = Provider.objects.all()[0]
        p.name = ''

        with self.assertRaises(ValidationError):
            p.full_clean()

    def test_str(self):
        p = Provider.objects.all()[0]
        p.name = "test"

        self.assertEquals(str(p),
                          "{} ({})".format("test", p.base_provider.name))
