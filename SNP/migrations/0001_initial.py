# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SNP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trait', models.CharField(max_length=255)),
                ('functional_snps', models.CharField(max_length=255)),
                ('tag_snps', models.CharField(max_length=255)),
                ('reference', models.CharField(max_length=255)),
            ],
        ),
    ]