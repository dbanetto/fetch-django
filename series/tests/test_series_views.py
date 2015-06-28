import json

from django.test import TestCase, Client

from series.models import Series


class TestSeriesViews(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]


    def test_json_index(self):
        c = Client(CONTENT_TYPE='application/json')

        res = c.get('/series/')
        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode(res.charset))
