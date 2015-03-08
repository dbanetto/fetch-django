# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the media type', max_length=80)),
                ('available_options', models.TextField(default='id', help_text='A CSV list of options that the media type allows')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='series',
            name='current_count',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 8, 8, 32, 24, 273375, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='media_type',
            field=models.ForeignKey(to='series.MediaType', help_text="Series' media type", default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='media_type_options',
            field=json_field.fields.JSONField(blank=True, default='null', help_text='A JSON object of options made avalible from the media type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='poster',
            field=models.ImageField(blank=True, upload_to=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='provider_options',
            field=json_field.fields.JSONField(blank=True, default='null', help_text='A JSON object of options made avalible from the provider'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 8, 8, 32, 24, 273332, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='series',
            name='total_count',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
