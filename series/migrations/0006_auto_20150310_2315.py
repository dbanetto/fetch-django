# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_auto_20150310_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.datetime(2015, 3, 10, 10, 15, 18, 584184, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.datetime(2015, 3, 10, 10, 15, 18, 584143, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
