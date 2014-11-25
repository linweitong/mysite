# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vs.models


class Migration(migrations.Migration):

    dependencies = [
        ('vs', '0007_auto_20141125_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placevideo',
            name='thumbnail',
            field=models.FileField(default='', upload_to=vs.models.thumbnail_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='placevideo',
            name='video',
            field=models.FileField(upload_to=vs.models.video_path),
            preserve_default=True,
        ),
    ]
