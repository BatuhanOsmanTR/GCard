# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20170726_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.URLField(default='http://lorempixel.com/600/400/sports/'),
        ),
    ]
