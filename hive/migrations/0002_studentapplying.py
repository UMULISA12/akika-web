# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-07 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hive', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentApplying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
