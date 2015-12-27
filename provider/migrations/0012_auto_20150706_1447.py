# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.validators
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0011_auto_20150623_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprovider',
            name='available_options',
            field=jsonfield.fields.JSONField(validators=[app.validators.json_schema_validator], default='{"properties": {"id": {"title": "id", "type": "integer", "required": false}}}', help_text='A JSON Schema of options that the base provider allows'),
        ),
    ]
