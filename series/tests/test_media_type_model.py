from django.test import TestCase

from series.models import MediaType


class MediaTypeModelTest(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]

    def test_str(self):
        m = MediaType.objects.all()[0]

        m.name = "test"

        self.assertEqual(str(m), "test")

    def test_get_available_options(self):
        m = MediaType.objects.all()[0]

        m.available_options = "1,2,3,4"

        self.assertEqual(m.get_available_options(), ['1', '2', '3', '4'])
