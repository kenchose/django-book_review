# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-09 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0042_auto_20190508_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, default='book_image/default-book.png', null=True, upload_to='book_image'),
        ),
    ]
