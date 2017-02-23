# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_phone_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonesold',
            name='phone',
        ),
        migrations.AddField(
            model_name='phonesold',
            name='product',
            field=models.CharField(max_length=20, null=True),
        ),
    ]