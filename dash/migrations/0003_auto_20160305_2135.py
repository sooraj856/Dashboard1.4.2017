# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_task_item_task_actual'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_item',
            name='task_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task_item',
            name='task_time',
            field=models.TimeField(null=True),
        ),
    ]
