import json

from django.test import TestCase, Client

from series.models import Series


class TestSeriesViews(TestCase):
    fixtures = ["test_series.json", "test_provider.json"]

    def test_index_json(self):
        c = Client(CONTENT_TYPE='application/json')

        res = c.get('/series/')

        self.assertTemplateUsed(res, 'series/index.json')

        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode(res.charset))

    def test_index_html(self):
        c = Client()

        res = c.get('/series/')

        self.assertTemplateUsed(res, 'series/index.html')

        self.assertEquals(res.status_code, 200)

    def test_index_mediatype_json(self):
        c = Client(CONTENT_TYPE='application/json')

        res = c.get('/series/media/')

        self.assertTemplateUsed(res, 'series/media_index.json')

        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode(res.charset))

    def test_index_mediatype_html(self):
        c = Client()

        res = c.get('/series/media/')

        self.assertTemplateUsed(res, 'series/media_index.html')

        self.assertEquals(res.status_code, 200)

    def test_view_html(self):
        c = Client()

        res = c.get('/series/1/')

        self.assertTemplateUsed(res, 'series/view.html')

        self.assertEquals(res.status_code, 200)

    def test_index_contains_entry(self):
        c = Client()

        res = c.get('/series/')
        html = res.content.decode(res.charset)
        self.assertTrue('Test Case' in html)
