import json

from django.test import TestCase, Client

from provider.models import Provider, BaseProvider

class TestProviderViews(TestCase):
    fixtures = ['test_provider.json']

    def test_index_html(self):
        c = Client()

        res = c.get('/provider/')

        self.assertEquals(res.templates[0].name, 'provider/index.html')
        self.assertEquals(res.status_code, 200)

    def test_index_json(self):
        c = Client()

        res = c.get('/provider/', CONTENT_TYPE='application/json')

        self.assertEquals(res.templates[0].name, 'provider/index.json')

        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode())

    def test_view(self):
        c = Client()
        p = Provider.objects.all()[0]
        res = c.get('/provider/' + str(p.id) + '/')

        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.templates[0].name, 'provider/view.html')

    def test_edit_get(self):
        c = Client()
        p = Provider.objects.all()[0]
        res = c.get('/provider/' + str(p.id) + '/edit/')

        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.templates[0].name, 'provider/edit.html')

    def test_view_nonexisting(self):
        c = Client()
        p = Provider.objects.all()[0]
        res = c.get('/provider/-1/')

        self.assertEquals(res.status_code, 404)

    def test_new_get(self):
        c = Client()

        res = c.get('/provider/new/')

        self.assertEquals(res.status_code, 200)
        self.assertEquals(res.templates[0].name, 'provider/new.html')
