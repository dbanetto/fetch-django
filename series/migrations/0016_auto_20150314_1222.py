# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0015_auto_20150313_1903'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ReleaseSchedule',
        ),
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(null=True, default=None),
            preserve_default=True,
        ),
    ]
