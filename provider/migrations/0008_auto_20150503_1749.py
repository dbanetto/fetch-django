# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0007_remove_provider_available_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprovider',
            name='available_options',
            field=jsonfield.fields.JSONField(default='{"id":{"type":"integer","required":false}}', help_text='A CSV list of options that the base provider allows'),
        ),
    ]
