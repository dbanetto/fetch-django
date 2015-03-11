from django.test import TestCase

from provider.models import BaseProvider


class BaseProviderTests(TestCase):
    fixtures = ['test_provider.json']

    def test_get_avianle_options(self):
        bp = BaseProvider(name="test",
                          available_options="id,query,location")

        self.assertEqual(['id', 'query', 'location'],
                         bp.get_available_options())

    def test_as_dict(self):
        prov = BaseProvider.objects.all()[0]
        prov_dict = prov.as_dict()

        self.assertTrue('name' in prov_dict)
        self.assertTrue('available_options' in prov_dict)

        self.assertEquals(prov.name, prov_dict['name'])
        self.assertEquals(prov.get_available_options(), prov_dict['available_options'])
