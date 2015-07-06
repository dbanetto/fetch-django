# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import series.models
from django.utils.timezone import utc
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0009_auto_20150311_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseSchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=80, help_text='Name of the media type')),
                ('available_options', models.TextField(default='id', help_text='A CSV list of options that the media type allows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='mediatype',
            name='available_options',
            field=models.TextField(default='id', help_text='A CSV list of options that the media type allows'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 9, 17, 47, 284858, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='media_type',
            field=models.ForeignKey(to='series.MediaType', help_text="Series' media type"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='media_type_options',
            field=json_field.fields.JSONField(default='null', help_text='A JSON object of options made available from the media type'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='poster',
            field=models.ImageField(upload_to=series.util.poster_path),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='release_schedule_options',
            field=json_field.fields.JSONField(default='null', help_text='A JSON object of needed info for each type of release schedule'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 9, 17, 47, 284796, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
