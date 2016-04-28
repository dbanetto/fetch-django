# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0009_auto_20150623_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprovider',
            name='available_options',
            field=jsonfield.fields.JSONField(help_text='A JSON Schema of options that the base provider allows', default={'id': {'required': False, 'type': 'integer'}}),
        ),
    ]
