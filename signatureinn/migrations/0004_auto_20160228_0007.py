# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-27 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signatureinn', '0003_expense_total_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtaRev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ota_amt', models.IntegerField(blank=True, null=True)),
                ('ota_category', models.CharField(blank=True, max_length=50, null=True)),
                ('total_ota_rev', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='day',
            name='card_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='cash_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='counter_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='date_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='expense_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='revenue',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='day',
            name='revenue_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='bills_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='bills_text_expense',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='bulk_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='bulk_text_expense',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date_expense',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='diesel_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='inventory_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='inventory_text_expense',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='maintainence_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='maintainence_text_expense',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='salary_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='salary_text_expense',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='total_expense',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
