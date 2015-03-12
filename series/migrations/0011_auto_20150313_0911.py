# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import json_field.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0010_auto_20150312_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 11, 27, 210881, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='media_type_options',
            field=json_field.fields.JSONField(help_text='A JSON object of options made available from the media type', default='null', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='release_schedule_options',
            field=json_field.fields.JSONField(help_text='A JSON object of needed info for each type of release schedule', default='null', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 11, 27, 210841, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
