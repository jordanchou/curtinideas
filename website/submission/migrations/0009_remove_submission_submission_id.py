# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 12:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0008_auto_20160410_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='submission_id',
        ),
    ]
