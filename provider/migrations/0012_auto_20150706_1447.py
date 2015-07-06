# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.validators
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0011_auto_20150623_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprovider',
            name='available_options',
            field=json_field.fields.JSONField(validators=[app.validators.json_schema_validator], default='{"properties": {"id": {"title": "id", "type": "integer", "required": false}}}', help_text='A JSON Schema of options that the base provider allows'),
        ),
    ]
