# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-23 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0017_auto_20160421_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='links',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
