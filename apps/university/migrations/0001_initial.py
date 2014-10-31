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
                ('status', models.CharField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prefix', models.TextField(max_length=10)),
                ('number', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=150)),
                ('hours', models.IntegerField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=40)),
                ('course', models.ForeignKey(to='university.Courses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campus', models.CharField(max_length=30)),
                ('building', models.CharField(max_length=30)),
                ('room', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('student_id', models.IntegerField(max_length=10)),
                ('student_major', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=40)),
                ('total_hours', models.IntegerField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='courses',
            name='location',
            field=models.ForeignKey(to='university.Locations'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classes',
            name='course',
            field=models.ForeignKey(to='university.Courses'),
            preserve_default=True,
        ),
    ]
