# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-16 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_category',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_location',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
