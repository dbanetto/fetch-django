from django.test import TestCase

from series.models import Series

class SeriesModelTest(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]

    def test_url_domain(self):
        s = Series.objects.all()[0]

        for url, domain in [('http://example.com/','example.com',),
                            ('http://example.com','example.com',),
                            ('https://example.com/','example.com',),
                            ('https://example.com','example.com',),
                            ('http://example.com/url/more/stuff','example.com',),
                            ('http://example.com/url/?get=true','example.com',),
                            ]:

            with self.subTest(url=url, domain=domain):
                s.info_url = url
                self.assertEqual(s.info_url_domain(), domain)
