# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-11 00:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0008_auto_20180709_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
