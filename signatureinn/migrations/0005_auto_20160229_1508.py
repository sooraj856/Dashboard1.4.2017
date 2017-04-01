# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-29 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signatureinn', '0004_auto_20160228_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='revenue',
            new_name='act_revenue_day',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='revenue_day',
            new_name='bank_day',
        ),
        migrations.AddField(
            model_name='day',
            name='daily_total_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='day',
            name='ota_revenue_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='day',
            name='total_revenue_day',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
