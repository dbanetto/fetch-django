# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0010_auto_20150623_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprovider',
            name='available_options',
            field=json_field.fields.JSONField(default='{"properties": {"id": {"type": "integer", "required": false, "title": "id"}}}', help_text='A JSON Schema of options that the base provider allows'),
        ),
    ]
