# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 06:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_commentmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessiontoken',
            name='last_request_on',
        ),
    ]
