# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-17 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0024_auto_20180717_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, default='book_img/default-book.png', upload_to='profile_image'),
        ),
    ]
