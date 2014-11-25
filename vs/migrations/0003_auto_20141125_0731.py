# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vs', '0002_auto_20141124_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('thumbnail', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('geo_latitude', models.FloatField()),
                ('geo_longitude', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(to='vs.Place')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.RemoveField(
            model_name='video',
            name='file',
        ),
        migrations.RemoveField(
            model_name='video',
            name='geo_latitude',
        ),
        migrations.RemoveField(
            model_name='video',
            name='geo_longitude',
        ),
        migrations.RemoveField(
            model_name='video',
            name='location',
        ),
        migrations.RemoveField(
            model_name='video',
            name='place',
        ),
        migrations.RemoveField(
            model_name='video',
            name='thumbnail',
        ),
        migrations.RemoveField(
            model_name='video',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='video',
            name='video',
            field=models.FileField(default='', upload_to=b'videos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_on',
            field=models.ForeignKey(to='vs.PlaceVideo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
