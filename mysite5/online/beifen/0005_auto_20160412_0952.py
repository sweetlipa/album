# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 01:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0004_auto_20160329_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='item',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='uid',
        ),
    ]