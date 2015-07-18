# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_text', models.CharField(default=b'default', max_length=250)),
                ('hideBit', models.IntegerField(default=0, max_length=1)),
                ('likes', models.IntegerField(default=0)),
                ('name', models.CharField(default=0, max_length=20)),
                ('timeStamp', models.DateTimeField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_name', models.CharField(unique=True, max_length=45)),
                ('courseDesc', models.CharField(max_length=100)),
                ('courseFee', models.IntegerField(null=True)),
                ('createdTS', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('hideBit', models.IntegerField(default=1, max_length=1)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('professor', models.CharField(default=b'null', max_length=40, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_name', models.CharField(unique=True, max_length=45)),
                ('lessonDesc', models.CharField(max_length=100)),
                ('createdTS', models.DateTimeField(auto_now_add=True)),
                ('hideBit', models.IntegerField(default=1, max_length=1)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('courseString', models.CharField(default=b'null', max_length=20, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('course', models.ForeignKey(to='Newsfeed.course', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(default=b'Student', max_length=20)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('phone_number', models.CharField(max_length=20)),
                ('isActive', models.IntegerField(default=0, max_length=1)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0, null=True)),
                ('hideBit', models.IntegerField(default=0, null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PeopleCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='Newsfeed.course')),
                ('peopleId', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like', models.CharField(max_length=10)),
                ('rate', models.IntegerField()),
                ('comment', models.ForeignKey(to='Newsfeed.comment')),
                ('people', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='recommendedList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommendedClass', models.ForeignKey(to='Newsfeed.course')),
                ('student', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='wishList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(to='Newsfeed.People')),
                ('wishListClass', models.ForeignKey(to='Newsfeed.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(to='Newsfeed.course', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='lesson',
            field=models.ForeignKey(to='Newsfeed.lesson', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='parentId',
            field=models.ForeignKey(to='Newsfeed.comment', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='professor',
            field=models.ForeignKey(to='Newsfeed.People', null=True),
            preserve_default=True,
        ),
    ]
