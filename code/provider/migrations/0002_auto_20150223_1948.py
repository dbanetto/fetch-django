# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseprovider',
            name='media_types',
            field=select_multiple_field.models.SelectMultipleField(verbose_name='Media types', choices=[('TV', 'TV Show'), ('PD', 'Podcast'), ('CM', 'Comic'), ('??', 'Unknown')], default='??', max_length=8),
            preserve_default=True,
        ),
    ]
