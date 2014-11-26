# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vs.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(null=True)),
                ('type', models.IntegerField(choices=[(1, b'like'), (2, b'comments')])),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
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
                ('type', models.IntegerField(choices=[(1, b'Club'), (2, b'Coffee')])),
                ('location', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('additionInfo', models.TextField(null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaceVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.FileField(upload_to=vs.models.thumbnail_path)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('video', models.FileField(upload_to=vs.models.video_path)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('updatedDate', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VSUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('thirdPartId', models.BigIntegerField(null=True)),
                ('thirdPartAccessToken', models.CharField(max_length=400, null=True)),
                ('accessToken', models.CharField(max_length=200, null=True)),
                ('firstName', models.CharField(max_length=200, null=True)),
                ('lastName', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('profileImage', models.CharField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='placevideo',
            name='creator',
            field=models.ForeignKey(to='vs.VSUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='placevideo',
            name='place',
            field=models.ForeignKey(to='vs.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='creator',
            field=models.ForeignKey(to='vs.VSUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(to='vs.VSUser'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(to='vs.PlaceVideo'),
            preserve_default=True,
        ),
    ]
