# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20150223_1948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseprovider',
            name='media_types',
        ),
    ]
