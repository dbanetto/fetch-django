from os import path

from django.test import TestCase
from django.conf import settings

from app.storage import OverwriteStorage

class TestOverwriteStorage(TestCase):

    def test_get_avianle_name(self):
        ow = OverwriteStorage()

        self.assertEquals("test.txt",
                          ow.get_available_name("test.txt"))

    def test_get_aviable_name_existing(self):
        ow = OverwriteStorage()

        with open(path.join(settings.MEDIA_ROOT, "test.txt"), 'w') as f:
            f.write("1")
            f.flush()

        self.assertEquals("test.txt",
                          ow.get_available_name("test.txt"))

        self.assertFalse(ow.exists("test.txt"))

