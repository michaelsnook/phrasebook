# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_remove_deck_learning'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='cards',
            field=models.ManyToManyField(blank=True, to='cards.Card'),
        ),
    ]
