# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170221_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
