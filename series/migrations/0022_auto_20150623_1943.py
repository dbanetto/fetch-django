# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0021_series_info_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediatype',
            name='available_options',
        ),
        migrations.AddField(
            model_name='mediatype',
            name='options',
            field=models.TextField(help_text='A JSON schema of options that the media type allows', default='id'),
        ),
    ]
