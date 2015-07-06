# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import series.models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_auto_20150309_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 8, 22, 34, 1, 203784, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='poster',
            field=models.ImageField(upload_to=series.util.poster_path, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 8, 22, 34, 1, 203733, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
