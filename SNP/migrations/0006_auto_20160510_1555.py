# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SNP', '0005_snp_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snp',
            name='reference',
            field=models.URLField(default='NONE', max_length=255),
        ),
    ]