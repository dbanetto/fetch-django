# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0006_auto_20150308_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='available_options',
        ),
    ]
