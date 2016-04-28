# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0003_remove_baseprovider_media_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseprovider',
            name='avaiable_options',
            field=models.TextField(default='quality', help_text='A CSV list of options that the base provider allows'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='provider',
            name='regex_find_count',
            field=models.CharField(max_length=256, default='\\d+', help_text='Regular expression used client side to extract the episode/chapter count from a file name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='provider',
            name='website',
            field=models.URLField(verbose_name="Provider's website", help_text="url to the provider's website"),
            preserve_default=True,
        ),
    ]
