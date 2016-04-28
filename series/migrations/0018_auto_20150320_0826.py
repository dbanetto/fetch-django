# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0017_series_release_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='series',
            name='search_title',
            field=models.CharField(verbose_name='String to be used when searching for the series', max_length=256, default=''),
            preserve_default=False,
        ),
    ]
