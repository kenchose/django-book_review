# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-05-09 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0037_auto_20190508_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_img',
            field=models.ImageField(blank=True, default='/profile/media/book_image/default-book.png', upload_to='book_image'),
        ),
    ]
