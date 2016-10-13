# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 12:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0012_auto_20161013_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='languages',
        ),
        migrations.AddField(
            model_name='person',
            name='speaks_languages',
            field=models.ManyToManyField(related_name='speakers', to='cards.Language'),
        ),
        migrations.AddField(
            model_name='person',
            name='studying_languages',
            field=models.ManyToManyField(related_name='students', to='cards.Language'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
