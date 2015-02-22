from django.test import TestCase

from provider.models import BaseProvider


class BaseProviderMethodTests(TestCase):

    def test_get_media_type_csv(self):
        """
        Test if valid CSV strings are produced
        """
        b = BaseProvider(name="base")
        self.assertEqual("??", b.get_media_types_csv())
        b = BaseProvider(name="base", media_types=['??', 'TV'])
        self.assertEqual("??,TV", b.get_media_types_csv())
