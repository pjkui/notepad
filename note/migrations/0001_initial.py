# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('color', models.CharField(max_length=10)),
                ('authorID', models.IntegerField()),
                ('noteType', models.IntegerField()),
                ('createTime', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NoteAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('noteID', models.ForeignKey(to='note.Note')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('nickname', models.CharField(max_length=40)),
                ('loginIP', models.CharField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='noteauthor',
            name='userID',
            field=models.ForeignKey(to='note.User'),
        ),
    ]
