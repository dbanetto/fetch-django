from datetime import datetime, timedelta

from django.test import TestCase, Client

from series.models import Series


class TestAppViews(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]

    def test_index_html(self):
        c = Client()

        # Ensure one card is made
        s = Series.objects.all()[0]
        s.start_date = datetime.now() + timedelta(days=-6)
        s.end_date = None
        s.release_schedule = 'W'
        s.save()

        next = s.next_release()
        self.assertTrue(next is not None and next < datetime.now() + timedelta(days=7))

        res = c.get('/')

        self.assertEquals(res.status_code, 200)

        expect_templates = ['app/index.html', 'series/series_card.html']
        for t in res.templates:
            if t.name in expect_templates:
                expect_templates.remove(t.name)

        self.assertEquals(len(expect_templates), 0)
