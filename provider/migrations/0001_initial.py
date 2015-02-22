# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('media_types', select_multiple_field.models.SelectMultipleField(default='??', verbose_name='Media types', choices=[('TV', 'TV Show'), ('PD', 'Podcast'), ('CM', 'Comic'), ('??', 'Unknown')], max_length=4)),
                ('name', models.CharField(verbose_name="Base Provider's name", max_length=160)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name of the provider', max_length=160)),
                ('website', models.CharField(verbose_name="Provider's website", max_length=250)),
                ('base_provider', models.ForeignKey(to='provider.BaseProvider')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
