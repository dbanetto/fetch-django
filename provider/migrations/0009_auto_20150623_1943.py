# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0008_auto_20150503_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprovider',
            name='available_options',
            field=json_field.fields.JSONField(help_text='A JSON Schema of options that the base provider allows', default='{"id":{"type":"integer","required":false}}'),
        ),
    ]
