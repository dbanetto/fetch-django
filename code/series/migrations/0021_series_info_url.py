# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0020_auto_20150321_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='info_url',
            field=models.URLField(verbose_name='Information URL', blank=True),
            preserve_default=True,
        ),
    ]
