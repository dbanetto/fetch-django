from django.test import TestCase
from django.core.validators import ValidationError

from provider.models import BaseProvider


class BaseProviderTests(TestCase):
    fixtures = ['test_provider.json']

    def test_get_available_options(self):
        bp = BaseProvider(name="test",
                          available_options="id,query,location")

        self.assertEqual(['id', 'query', 'location'],
                         bp.get_available_options())

    def test_name_max_length(self):
        prov = BaseProvider(name='*'*161)
        with self.assertRaises(ValidationError):
            prov.full_clean()

    def test_name_empty(self):
        prov = BaseProvider(name='')
        with self.assertRaises(ValidationError):
            prov.full_clean()
