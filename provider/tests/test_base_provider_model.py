from django.test import TestCase

from provider.models import BaseProvider


class BaseProviderTests(TestCase):

    def test_get_avianle_options(self):
        bp = BaseProvider(name="test",
                          available_options="id,query,location")

        self.assertEqual(['id', 'query', 'location'],
                         bp.get_available_options())
