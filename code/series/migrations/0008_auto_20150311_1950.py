# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0007_auto_20150311_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 6, 50, 40, 788911, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 11, 6, 50, 40, 788865, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
