# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
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
                ('geo_latitude', models.FloatField()),
                ('geo_longitude', models.FloatField()),
                ('addition_info', models.TextField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.CharField(max_length=200)),
                ('file', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('geo_latitude', models.FloatField()),
                ('geo_longitude', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
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
                ('thirdPartAccessToken', models.CharField(max_length=200, null=True)),
                ('accessToken', models.CharField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='video',
            name='creator',
            field=models.ForeignKey(related_name='videos', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='video',
            name='place',
            field=models.ForeignKey(related_name='videos', to='vs.Place'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_on',
            field=models.ForeignKey(to='vs.Video'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(related_name='videos+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
