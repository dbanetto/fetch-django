import json

from django.test import TestCase
from django.core.validators import ValidationError

from provider.models import BaseProvider


class BaseProviderTests(TestCase):
    fixtures = ['test_provider.json']

    def test_available_options_json(self):
        bp = BaseProvider(name="test",
                          available_options={'id':{'type':'integer','required':False}})

        self.assertEqual(json.dumps({'id':{'type':'integer','required':False}}),
                         bp.available_options_json())

    def test_name_max_length(self):
        prov = BaseProvider(name='*'*161)
        with self.assertRaises(ValidationError):
            prov.full_clean()

    def test_name_empty(self):
        prov = BaseProvider(name='')
        with self.assertRaises(ValidationError):
            prov.full_clean()

    def test_str(self):
        p = BaseProvider.objects.all()[0]
        p.name = "test"

        self.assertEquals(str(p), "test")
