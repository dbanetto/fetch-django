# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0018_auto_20150320_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='save_path',
            field=models.CharField(null=True, verbose_name='Path to be sorted into', max_length=256),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='search_title',
            field=models.CharField(null=True, verbose_name='String to be used when searching for the series', max_length=256),
            preserve_default=True,
        ),
    ]
