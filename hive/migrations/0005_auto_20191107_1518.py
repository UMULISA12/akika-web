# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-07 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hive', '0004_businessentapplying'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessentapplying',
            old_name='business_number',
            new_name='contact_number',
        ),
    ]