# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import series.models
import datetime
import app.storage
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0011_auto_20150313_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 25, 41, 178448, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='poster',
            field=models.ImageField(upload_to=series.util.poster_path, storage=app.storage.OverwriteStorage()),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='series',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 12, 20, 25, 41, 178406, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
