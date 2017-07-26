# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20170725_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='digits',
            field=models.CharField(default=payment.models.card_digit_gen, max_length=8),
        ),
        migrations.AlterField(
            model_name='paymentcard',
            name='digits',
            field=models.CharField(default=payment.models.paymentcard_digit_gen, max_length=10),
        ),
    ]