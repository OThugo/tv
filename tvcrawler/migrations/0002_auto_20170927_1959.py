# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-27 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvcrawler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]