from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

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
                            ('ftp://example.com/url/more/stuff','example.com',),
                            ('madeprotocal://www.example.com/url/?get=true','www.example.com',),
                            ]:

            with self.subTest(url=url, domain=domain):
                s.info_url = url
                self.assertEqual(s.info_url_domain(), domain)

    def test_has_started(self):
        s = Series.objects.all()[0]
        for start, val in [(timezone.now().date() + timedelta(days=7), False),
                            (timezone.now().date() + timedelta(days=-7), True),
                            (timezone.now().date(), True),
                          ]:
            s.start_date = start
            with self.subTest(start_date=start, val=val):
                self.assertEqual(val, s.has_started())

    def test_has_ended(self):
        s = Series.objects.all()[0]
        for end, val in [(timezone.now().date() + timedelta(days=7), False),
                         (timezone.now().date() + timedelta(days=-7), True),
                         (timezone.now().date(), False),
                        ]:
            s.end_date = end
            with self.subTest(end_date=end, val=val):
                self.assertEqual(val, s.has_ended())

    def test_is_airing(self):
        s = Series.objects.all()[0]

        for start, end, val in [(timezone.now().date() + timedelta(days=7), None, False),
                                (timezone.now().date() + timedelta(days=-7), None, True),
                                (timezone.now().date(), None, True),
                                (timezone.now().date() + timedelta(days=7), timezone.now().date() + timedelta(days=8), False),
                                (timezone.now().date() + timedelta(days=-7), timezone.now().date() + timedelta(days=7), True),
                                (timezone.now().date(), timezone.now().date(), True),
                                ]:
            s.start_date = start
            s.end_date = end
            with self.subTest(start_date=start, end_date=end, val=val):
                self.assertEqual(val, s.is_airing())
