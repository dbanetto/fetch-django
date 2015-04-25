from datetime import timedelta, time, datetime

from django.test import TestCase
from django.core.validators import ValidationError

from series.models import Series


class SeriesModelTest(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]

    def test_url_domain(self):
        s = Series.objects.all()[0]

        for url, domain in [
            ('http://example.com/', 'example.com',),
            ('http://example.com', 'example.com',),
            ('https://example.com/', 'example.com',),
            ('https://example.com', 'example.com',),
            ('http://example.com/url/more/stuff', 'example.com',),
            ('http://example.com/url/?get=true', 'example.com',),
            ('ftp://example.com/url/more/stuff', 'example.com',),
            ('madeprotocal://www.example.com/url/?get=true', 'www.example.com',),
        ]:

            with self.subTest(url=url, domain=domain):
                s.info_url = url
                self.assertEqual(s.info_url_domain(), domain)

    def test_has_started(self):
        s = Series.objects.all()[0]
        for start, rtime, val in [
            (datetime.now().date() + timedelta(days=7), time.min, False),
            (datetime.now().date() + timedelta(days=-7), time.min, True),
            (datetime.now().date(), time.min, True),
            (datetime.now().date(), time.max, False),
            (None, time.min, False),
        ]:
            s.start_date = start
            s.release_time = rtime
            with self.subTest(start_date=start, rtime=rtime, val=val):
                self.assertEqual(val, s.has_started())

    def test_has_ended(self):
        s = Series.objects.all()[0]
        for end, rtime, val in [
            (datetime.now().date() + timedelta(days=7), time.min, False),
            (datetime.now().date() + timedelta(days=-7), time.min, True),
            (datetime.now().date(), time.min, True),
            (datetime.now().date(), time.max, False),
            (None, time.max, False),
        ]:
            s.end_date = end
            s.release_time = rtime
            with self.subTest(end_date=end, rtime=rtime, val=val):
                self.assertEqual(val, s.has_ended())

    def test_is_airing(self):
        s = Series.objects.all()[0]

        for start, end, rtime, val in [
            (datetime.now().date() + timedelta(days=7), None, time.min, False),
            (datetime.now().date() + timedelta(days=-7), None, time.min, True),
            (datetime.now().date(), None, time.min, True),
            (datetime.now().date(), None, time.max, False),
            (datetime.now().date() + timedelta(days=7),
                datetime.now().date() + timedelta(days=8), time.min, False),
            (datetime.now().date() + timedelta(days=-7),
                datetime.now().date() + timedelta(days=7), time.min, True),
            (datetime.now().date(), datetime.now().date(), time.min, False),
            (datetime.now().date(), datetime.now().date(), time.max, False),
        ]:
            s.start_date = start
            s.end_date = end
            s.release_time = rtime
            with self.subTest(start_date=start, end_date=end, rtime=rtime,
                              val=val):
                self.assertEqual(val, s.is_airing())

    def test_curent_count_and_total(self):
        s = Series.objects.all()[0]

        for current, total, error in [
            (2,  1, True),
            (1,  2, False),
            (1,  1, False),
            (10, 0, False),
            (-1, 0, True),
            (1, -1, True),
        ]:
            s.current_count = current
            s.total_count = total
            if error:
                with self.assertRaises(ValidationError):
                    s.clean()
            else:
                s.clean()
