# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-08 06:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0034_auto_20190507_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_img_url',
        ),
    ]
