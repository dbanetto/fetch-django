# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0019_auto_20150321_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='save_path',
            field=models.CharField(blank=True, default='', verbose_name='Path to be sorted into', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='search_title',
            field=models.CharField(blank=True, default='', verbose_name='String to be used when searching for the series', max_length=256),
            preserve_default=True,
        ),
    ]
