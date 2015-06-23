# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0024_auto_20150623_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediatype',
            name='available_options',
            field=json_field.fields.JSONField(default='{"properties": {"id": {"type": "integer", "required": false, "title": "id"}}}', help_text='A JSON schema of options that the media type allows'),
        ),
    ]
