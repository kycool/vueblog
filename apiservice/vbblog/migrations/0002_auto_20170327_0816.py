# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 08:16
from __future__ import unicode_literals

import apiservice.utils.uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.CharField(default=apiservice.utils.uuid.UUIDTools.uuid1_hex, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='articletagship',
            name='id',
            field=models.CharField(default=apiservice.utils.uuid.UUIDTools.uuid1_hex, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default=apiservice.utils.uuid.UUIDTools.uuid1_hex, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='systemmeta',
            name='id',
            field=models.CharField(default=apiservice.utils.uuid.UUIDTools.uuid1_hex, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.CharField(default=apiservice.utils.uuid.UUIDTools.uuid1_hex, editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]
