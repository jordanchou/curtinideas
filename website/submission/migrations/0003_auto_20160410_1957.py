# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_submission_submission_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_id',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
