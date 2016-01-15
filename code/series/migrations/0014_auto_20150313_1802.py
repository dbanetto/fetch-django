# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0013_auto_20150313_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 5, 2, 8, 297857, tzinfo=utc), null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 13, 5, 2, 8, 297816, tzinfo=utc), null=True),
            preserve_default=True,
        ),
    ]
