# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0008_auto_20150311_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='provider_options',
        ),
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 7, 2, 49, 301893, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 7, 2, 49, 301846, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
