# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20160410_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_id',
            field=models.PositiveSmallIntegerField(default=-1),
        ),
    ]