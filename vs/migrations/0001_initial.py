# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True)),
                ('type', models.IntegerField(choices=[(1, b'like'), (2, b'comments')])),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(related_name='videos+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, b'Club')])),
                ('location', models.CharField(max_length=200)),
                ('geo_latitude', models.FloatField()),
                ('geo_longitude', models.FloatField()),
                ('addition_info', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(related_name='places', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('videoThumbnail', models.CharField(max_length=200)),
                ('video', models.FileField(upload_to=b'')),
                ('location', models.CharField(max_length=200)),
                ('geo_latitude', models.FloatField()),
                ('geo_longitude', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(related_name='videos', to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(to='vs.Place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(to='vs.Video'),
            preserve_default=True,
        ),
    ]
