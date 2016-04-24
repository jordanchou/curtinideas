# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0018_submission_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='downvotes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='upvotes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]