# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_merge_20170912_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(db_index=True, help_text='The unique country code', unique=True)),
                ('short_code', models.TextField(db_index=True, help_text='The unique 2-character country code', unique=True)),
                ('name', models.TextField(help_text='The name of the region')),
                ('short_name', models.TextField(help_text='The short name of the region', null=True)),
                ('is_current', models.BooleanField(default=True, help_text='Boolean indicator if this country is current')),
                ('is_country', models.BooleanField(default=False, help_text='Boolean indicator if this region is a country')),
                ('is_territory', models.BooleanField(default=False, help_text='Boolean indicator if this region is a territory')),
            ],
            options={
                'ordering': ['code'],
                'managed': True,
            },
        ),
        migrations.RemoveField(
            model_name='location',
            name='country',
        ),
    ]