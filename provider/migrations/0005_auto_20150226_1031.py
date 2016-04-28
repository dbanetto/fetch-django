# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0004_auto_20150225_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='baseprovider',
            old_name='avaiable_options',
            new_name='available_options',
        ),
    ]
