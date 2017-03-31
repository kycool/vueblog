# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 07:49
from __future__ import unicode_literals

import apiservice.utils.uuid
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.UUIDField(default=apiservice.utils.uuid.UUIDTools.uuid1_hex, editable=False, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=20, verbose_name='配置键')),
                ('value', models.CharField(max_length=50, verbose_name='配置值')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用户元数据',
                'verbose_name_plural': '用户元数据',
            },
        ),
    ]