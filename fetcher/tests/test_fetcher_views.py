import json
from django.test import TestCase, Client


class TestFetcherViews(TestCase):

    def test_index_html(self):
        c = Client()

        res = c.get('/fetcher/')

        self.assertEquals(res.status_code, 200)

        expect_templates = ['fetcher/index.html']
        for t in res.templates:
            if t.name in expect_templates:
                expect_templates.remove(t.name)

        self.assertEquals(len(expect_templates), 0)

    def test_status_html_redirect(self):
        c = Client()

        res = c.get('/fetcher/status/')

        self.assertEquals(res.status_code, 302)

        self.assertEquals(len(res.templates), 0)
        self.assertTrue(res.url.endswith("/fetcher/"))

    def test_force_fetch_html_redirect(self):
        c = Client()

        res = c.get('/fetcher/force/fetch/')

        self.assertEquals(res.status_code, 302)

        self.assertEquals(len(res.templates), 0)
        self.assertTrue(res.url.endswith("/fetcher/"))

    def test_force_sort_html_redirect(self):
        c = Client()

        res = c.get('/fetcher/force/sort/')

        self.assertEquals(res.status_code, 302)

        self.assertEquals(len(res.templates), 0)
        self.assertTrue(res.url.endswith("/fetcher/"))

    def test_status_json_redirect(self):
        c = Client()

        res = c.post('/fetcher/status/', CONTENT_TYPE='application/json')

        self.assertEquals(res.status_code, 302)

        self.assertEquals(len(res.templates), 0)
        self.assertTrue(res.url.endswith("/fetcher/"))

    def test_force_fetch_json_redirect(self):
        c = Client(CONTENT_TYPE='application/json')

        res = c.get('/fetcher/force/fetch/')

        self.assertEquals(res.status_code, 302)

        self.assertEquals(len(res.templates), 0)
        self.assertTrue(res.url.endswith("/fetcher/"))

    def test_force_sort_json_redirect(self):
        c = Client(CONTENT_TYPE='application/json')

        res = c.get('/fetcher/force/fetch/')

        self.assertEquals(res.status_code, 302)

        self.assertEquals(len(res.templates), 0)
        self.assertTrue(res.url.endswith("/fetcher/"))

    def test_status_json(self):
        c = Client(CONTENT_TYPE='application/json')

        res = c.get('/fetcher/status/')

        self.assertEquals(res.status_code, 200)

        self.assertEquals(len(res.templates), 0)
        json.loads(res.content.decode(res.charset))

    def test_force_fetch_post_json(self):
        c = Client()

        res = c.post('/fetcher/force/fetch/', CONTENT_TYPE='application/json')

        self.assertEquals(res.status_code, 200)

        self.assertEquals(len(res.templates), 0)
        json.loads(res.content.decode(res.charset))

    def test_force_sort_post_json(self):
        c = Client(CONTENT_TYPE='application/json')

        res = c.post('/fetcher/force/sort/', CONTENT_TYPE='application/json')

        self.assertEquals(res.status_code, 200)

        self.assertEquals(len(res.templates), 0)
        json.loads(res.content.decode(res.charset))
