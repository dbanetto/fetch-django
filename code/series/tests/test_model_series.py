from datetime import timedelta, time, datetime
from dateutil.relativedelta import relativedelta

from django.test import TestCase
from django.core.validators import ValidationError
from django.utils.translation import ugettext as _

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
            ('fakepro://www.example.com/url/?get=true', 'www.example.com',),
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

    def test_has_ended_completed_episodes(self):
        s = Series.objects.all()[0]
        for current, total, val in [
            (0, 1, False),
            (1, 1, True),
            (25, 25, True),
        ]:
            s.end_date = None
            s.release_time = time.max
            s.current_count = current
            s.total_count = total
            with self.subTest(current=current, total=total, val=val):
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
            (-1, None, True),
            ( 1, None, False),
            (1, -1, True),
        ]:
            s.current_count = current
            s.total_count = total
            with self.subTest(current=current, total=total, error=error):
                if error:
                    with self.assertRaises(ValidationError):
                        s.clean()
                else:
                    s.clean()

    def test_end_date_greater_than_start(self):
        s = Series.objects.all()[0]

        s.start_date = datetime.now() + timedelta(days=+1)
        s.end_date = datetime.now() + timedelta(days=-1)

        with self.assertRaises(ValidationError):
            s.clean()

    def test_series_next_release(self):
        s = Series.objects.all()[0]

        for start, end, at, expected, schedule in [
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=7),
             time.max,
             datetime.combine(datetime.now().date(), time.max),
             Series.WEEKLY
             ),
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=7),
             time.max,
             datetime.combine(datetime.now().date() + timedelta(days=7), time.max),
             Series.FORTNIGHTLY
             ),
            (datetime.now().date() + relativedelta(months=-1),
             datetime.now().date() + relativedelta(months=1),
             time.max,
             datetime.combine(datetime.now().date(), time.max),
             Series.MONTHLY
             ),
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=-8),
             time.max,
             None,
             Series.WEEKLY
             ),
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=7),
             time.max,
             datetime.combine(datetime.now().date() + timedelta(days=7), time.max),
             Series.NONE
             ),
            (datetime.now().date() + timedelta(days=-7),
             None,
             time.max,
             None,
             Series.NONE
             ),

            (datetime.now().date() + timedelta(days=7),
             datetime.now().date() + timedelta(days=8),
             time.max,
             datetime.combine(datetime.now().date() + timedelta(days=7), time.max),
             Series.WEEKLY
             ),
            (None,
             None,
             time.max,
             None,
             Series.WEEKLY
             ),
        ]:
            s.start_date = start
            s.end_date = end
            s.release_time = at
            s.release_schedule = schedule
            with self.subTest(start=start, end=end, at=at,
                              schedule=schedule, epxected=expected):
                self.assertEqual(s.next_release(), expected)

    def test_label_text(self):
        s = Series.objects.all()[0]

        for start, end, expected in [
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=7),
             _('Airing')
             ),
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=-1),
             _('Finished')
             ),
            (datetime.now().date() + timedelta(days=7),
             datetime.now().date() + timedelta(days=8),
             _('Soon')
             ),
        ]:
            s.start_date = start
            s.end_date = end
            with self.subTest(start=start, end=end, expected=expected):
                self.assertEqual(s.label_text(), expected)

    def test_bootstrap_label_class(self):
        s = Series.objects.all()[0]

        for start, end, expected in [
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=7),
             'label-success'
             ),
            (datetime.now().date() + timedelta(days=-7),
             datetime.now().date() + timedelta(days=-1),
             'label-danger'
             ),
            (datetime.now().date() + timedelta(days=7),
             datetime.now().date() + timedelta(days=8),
             'label-info'
             ),
        ]:
            s.start_date = start
            s.end_date = end
            with self.subTest(start=start, end=end, expected=expected):
                self.assertEqual(s.bootstrap_label_class(), expected)

    def test_bootstrap_progress_bar(self):
        s = Series.objects.all()[0]

        for pb_class, val, max, current, total in [
            ('progress-bar-success', 50, 10, 5, 10),
            ('progress-bar-warning progress-bar-striped', 5, 5, 5, 0),
        ]:
            with self.subTest(pb_class=pb_class, val=val,
                              max=max, current=current, total=total):
                s.current_count = current
                s.total_count = total

                html = s.bootstrap_progressbar()

                self.assertTrue(pb_class in html, html)
                self.assertTrue(str(val) in html)
                self.assertTrue(str(max) in html)

    def test_str(self):
        s = Series.objects.all()[0]

        s.title = "test"

        self.assertEquals(str(s), "{} ({})".format(s.title, s.provider.name))


    def test_release_schedule_options(self):
        s = Series.objects.all()[0]
        s.release_schedule_options = {"test": "value"}

        self.assertEquals(s.release_schedule_options_json(),
                          '{"test": "value"}')

    def test_media_type_options(self):
        s = Series.objects.all()[0]
        s.media_type_options = {"test": "value"}

        self.assertEquals(s.media_type_options_json(),
                          '{"test": "value"}')

