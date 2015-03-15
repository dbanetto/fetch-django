# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0016_auto_20150314_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='release_time',
            field=models.TimeField(default=datetime.time(12, 0)),
            preserve_default=True,
        ),
    ]
