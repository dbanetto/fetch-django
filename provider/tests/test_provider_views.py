import json

from django.test import TestCase, Client

from provider.models import Provider


class TestProviderViews(TestCase):
    fixtures = ['test_provider.json']

    def test_index_html(self):
        c = Client()

        res = c.get('/provider/')

        self.assertEquals(res.status_code, 200)

        expect_templates = ['provider/index.html']
        for t in res.templates:
            if t.name in expect_templates:
                expect_templates.remove(t.name)

        self.assertEquals(len(expect_templates), 0)

    def test_index_json(self):
        c = Client()

        res = c.get('/provider/', CONTENT_TYPE='application/json')

        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode())

        expect_templates = ['provider/index.json']
        for t in res.templates:
            if t.name in expect_templates:
                expect_templates.remove(t.name)

        self.assertEquals(len(expect_templates), 0)
        json.loads(res.content.decode(res.charset))

    def test_view(self):
        c = Client()
        p = Provider.objects.all()[0]
        res = c.get('/provider/' + str(p.id) + '/')

        self.assertEquals(res.status_code, 200)

        expect_templates = ['provider/view.html']
        for t in res.templates:
            if t.name in expect_templates:
                expect_templates.remove(t.name)

        self.assertEquals(len(expect_templates), 0)

    def test_edit_get(self):
        c = Client()
        p = Provider.objects.all()[0]
        res = c.get('/provider/' + str(p.id) + '/edit/')

        self.assertEquals(res.status_code, 200)

        expect_templates = ['provider/edit.html',
                            'provider/form_provider.html']
        for t in res.templates:
            if t.name in expect_templates:
                expect_templates.remove(t.name)

        self.assertEquals(len(expect_templates), 0, expect_templates)

    def test_view_nonexisting(self):
        c = Client()
        res = c.get('/provider/0/')

        self.assertEquals(res.status_code, 404)

    def test_new_get(self):
        c = Client()

        res = c.get('/provider/new/')

        self.assertEquals(res.status_code, 200)

        expect_templates = ['provider/new.html', 'provider/form_provider.html']
        for t in res.templates:
            if t.name in expect_templates:
                expect_templates.remove(t.name)

        self.assertEquals(len(expect_templates), 0, expect_templates)
