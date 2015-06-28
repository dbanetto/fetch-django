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
