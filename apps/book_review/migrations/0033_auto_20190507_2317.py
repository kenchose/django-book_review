# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-08 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0032_book_book_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img_url',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
