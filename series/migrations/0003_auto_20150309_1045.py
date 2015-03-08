# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0002_auto_20150308_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediatype',
            name='available_options',
            field=models.TextField(help_text='A CSV list of options that the media type allows', blank=True, default='id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 8, 21, 45, 33, 932191, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='media_type_options',
            field=json_field.fields.JSONField(help_text='A JSON object of options made available from the media type', blank=True, default='null'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='poster',
            field=models.ImageField(blank=True, upload_to='series/posters'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='provider_options',
            field=json_field.fields.JSONField(help_text='A JSON object of options made available from the provider', blank=True, default='null'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 8, 21, 45, 33, 932138, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
