# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_auto_20150310_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 3, 11, 8, 615955, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 3, 11, 8, 615911, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
