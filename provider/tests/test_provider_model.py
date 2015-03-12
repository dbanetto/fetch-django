from django.test import TestCase

from provider.models import Provider


class ProviderMethodTests(TestCase):
    fixtures = ['test_provider.json']

    def test_get_avianle_options(self):
        prov = Provider.objects.filter(pk=1)[0]
        self.assertEqual(['quality','options'],
                         prov.get_available_options())
