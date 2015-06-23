# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0023_auto_20150623_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediatype',
            name='available_options',
            field=json_field.fields.JSONField(help_text='A JSON schema of options that the media type allows', default={'id': {'required': False, 'type': 'integer'}}),
        ),
    ]
