# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-08-06 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import model_managers.home_model_manager


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationTime', models.DateTimeField(auto_now_add=True)),
                ('IsActive', models.BooleanField(default=True)),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('Desc', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'team',
            },
            managers=[
                ('objects', model_managers.home_model_manager.TeamManager()),
            ],
        ),
        migrations.AddField(
            model_name='dictype',
            name='DicTypeValue',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='agent',
            name='CreationTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='CreationTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='webapps',
            name='CreationTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]