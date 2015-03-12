# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_auto_20150309_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='release_schedule',
            field=models.CharField(default='W', max_length=1, choices=[('N', 'None'), ('W', 'Weekly'), ('F', 'Fortnightly'), ('M', 'Monthly'), ('D', 'Discrete')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='release_schedule_options',
            field=json_field.fields.JSONField(help_text='A JSON object of needed info for each type of release schedule', default='null', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 10, 9, 13, 7, 251477, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 10, 9, 13, 7, 251433, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
