from django.test import TestCase

from series.util import poster_path


class TestSeriesUtil(TestCase):

    def test_poster_path(self):
        s = type('Dummy', (object,), {"id": 1})

        for name, useInstance, expected in [
            ("test.txt", False, "series/poster/test.txt"),
            ("test.txt", True, "series/poster/1.txt"),
            ("test", True, "series/poster/1"),
            ("test", False, "series/poster/test"),
        ]:
            with self.subTest(name=name,
                              useInstance=useInstance,
                              expected=expected):
                self.assertEquals(
                    poster_path(s if useInstance else None, name),
                    expected)
