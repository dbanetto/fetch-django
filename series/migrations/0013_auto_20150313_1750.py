# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0012_auto_20150313_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 4, 50, 11, 883068, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 4, 50, 11, 883024, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
