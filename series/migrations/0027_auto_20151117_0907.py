# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.storage
import series.util


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0026_auto_20150706_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='poster',
            field=models.ImageField(upload_to=series.util.poster_path, storage=app.storage.OverwriteStorage(), null=True),
        ),
    ]
