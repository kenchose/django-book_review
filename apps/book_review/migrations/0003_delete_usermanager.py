# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-04 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0002_usermanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserManager',
        ),
    ]
