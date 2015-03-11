import json

from django.test import TestCase

from provider.models import Provider


class ProviderMethodTests(TestCase):
    fixtures = ['test_provider.json']

    def test_get_avianle_options(self):
        prov = Provider.objects.filter(pk=1)[0]
        self.assertEqual(['quality','options'],
                         prov.get_available_options())

    def test_as_dict(self):
        prov = Provider.objects.all()[0]
        prov_dict = prov.as_dict()

        self.assertTrue('name' in prov_dict)
        self.assertTrue('website' in prov_dict)
        self.assertTrue('regex_find_count' in prov_dict)
        self.assertTrue('base_provider' in prov_dict)
        self.assertTrue('options' in prov_dict)
        self.assertTrue('available_options' in prov_dict)

        self.assertEquals(prov.name, prov_dict['name'])
        self.assertEquals(prov.website, prov_dict['website'])
        self.assertEquals(prov.regex_find_count, prov_dict['regex_find_count'])
        self.assertEquals(prov.base_provider.id, prov_dict['base_provider'])
        self.assertEquals(prov.get_available_options(), prov_dict['available_options'])
        self.assertEquals(json.dumps(prov.options), prov_dict['options'])
