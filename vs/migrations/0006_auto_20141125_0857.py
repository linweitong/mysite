# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vs', '0005_auto_20141125_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='creator',
        ),
        migrations.AddField(
            model_name='placevideo',
            name='creator',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='placevideo',
            name='video',
            field=models.FileField(upload_to=b'videos'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
