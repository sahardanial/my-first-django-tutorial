# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_phone_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='slug',
        ),
    ]