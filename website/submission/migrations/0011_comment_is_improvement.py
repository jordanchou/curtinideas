# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_improvement',
            field=models.BooleanField(default=False),
        ),
    ]
