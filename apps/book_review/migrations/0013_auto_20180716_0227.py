# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-16 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0012_auto_20180715_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='../../user_review/media/profile_image/profiledefault.png', upload_to='profile_image'),
        ),
    ]
