# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='submission_id',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
