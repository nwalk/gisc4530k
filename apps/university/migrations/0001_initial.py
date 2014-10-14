# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=40)),
                ('time_period', models.CharField(max_length=4)),
                ('university', models.CharField(max_length=40)),
                ('completion_date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('crn', models.IntegerField(max_length=4)),
                ('section', models.IntegerField(max_length=2)),
                ('course', models.CharField(max_length=10)),
                ('session', models.TextField(max_length=15)),
                ('title', models.CharField(max_length=40)),
                ('hours', models.IntegerField(max_length=1)),
                ('location', models.CharField(max_length=50)),
                ('instructor', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('status', models.CharField(max_length=40)),
                ('university', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campus', models.CharField(max_length=40)),
                ('building', models.CharField(max_length=40)),
                ('room', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('student_id', models.IntegerField(max_length=9)),
                ('student_major', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=40)),
                ('total_hours', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
