# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0022_auto_20150623_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediatype',
            name='options',
        ),
        migrations.AddField(
            model_name='mediatype',
            name='available_options',
            field=json_field.fields.JSONField(help_text='A JSON schema of options that the media type allows', default='{"id":{"type":"integer","required":false}}'),
        ),
    ]
