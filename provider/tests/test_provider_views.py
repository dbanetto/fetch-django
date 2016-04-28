import json

from django.test import TestCase, Client

from provider.models import Provider


class TestProviderViews(TestCase):
    fixtures = ['test_provider.json']

    def test_index_html(self):
        c = Client()

        res = c.get('/provider/')

        self.assertEquals(res.status_code, 200)

        self.assertTemplateUsed(res, 'provider/index.html')

    def test_index_json(self):
        c = Client()

        res = c.get('/provider/', CONTENT_TYPE='application/json')

        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode())

        self.assertTemplateUsed(res, 'provider/index.json')

        json.loads(res.content.decode(res.charset))

    def test_view(self):
        c = Client()
        p = Provider.objects.all()[0]
        res = c.get('/provider/' + str(p.id) + '/')

        self.assertEquals(res.status_code, 200)

        self.assertTemplateUsed(res, 'provider/view.html')

    def test_edit_get(self):
        c = Client()
        p = Provider.objects.all()[0]
        res = c.get('/provider/' + str(p.id) + '/edit/')

        self.assertEquals(res.status_code, 200)

        self.assertTemplateUsed(res, 'provider/edit.html')
        self.assertTemplateUsed(res, 'provider/form_provider.html')

    def test_view_nonexisting(self):
        c = Client()
        res = c.get('/provider/0/')

        self.assertEquals(res.status_code, 404)

    def test_new_get(self):
        c = Client()

        res = c.get('/provider/new/')

        self.assertEquals(res.status_code, 200)

        self.assertTemplateUsed(res, 'provider/new.html')
        self.assertTemplateUsed(res, 'provider/form_provider.html')

    def test_index_base_html(self):
        c = Client()

        res = c.get('/provider/base/')

        self.assertEquals(res.status_code, 200)

        self.assertTemplateUsed(res, 'provider/base_index.html')

    def test_index_base_json(self):
        c = Client()

        res = c.get('/provider/base/', CONTENT_TYPE='application/json')

        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode())

        self.assertTemplateUsed(res, 'provider/base_index.json')

        json.loads(res.content.decode(res.charset))

    def test_view_base_html(self):
        c = Client()

        res = c.get('/provider/base/1/')

        self.assertEquals(res.status_code, 200)

        self.assertTemplateUsed(res, 'provider/base_view.html')

    def test_view_base_json(self):
        c = Client()

        res = c.get('/provider/base/1/', CONTENT_TYPE='application/json')

        self.assertEquals(res.status_code, 200)
        json.loads(res.content.decode())

        self.assertTemplateUsed(res, 'provider/base_view.json')

        json.loads(res.content.decode(res.charset))
