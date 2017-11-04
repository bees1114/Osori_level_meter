# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-05 02:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Osori_rpg', '0002_auto_20171105_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('options', models.CharField(choices=[('Room_Visit', 'room_visit'), ('Event_Visit', 'event_visit'), ('Contribution', 'contribution')], max_length=100)),
                ('spec', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
