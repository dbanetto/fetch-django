# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0005_auto_20150226_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='available_options',
            field=models.TextField(default='quality', help_text='A CSV list of options that the provider allows'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='options',
            field=jsonfield.fields.JSONField(default='null', help_text="JSON Object filled of BaseProvider's available_options with data"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='baseprovider',
            name='available_options',
            field=models.TextField(default='id', help_text='A CSV list of options that the base provider allows'),
            preserve_default=True,
        ),
    ]
