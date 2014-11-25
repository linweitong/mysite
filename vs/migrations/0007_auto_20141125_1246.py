# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import vs.models


class Migration(migrations.Migration):

    dependencies = [
        ('vs', '0006_auto_20141125_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_on',
            new_name='video',
        ),
        migrations.AlterField(
            model_name='placevideo',
            name='video',
            field=models.FileField(upload_to=vs.models.file_path),
            preserve_default=True,
        ),
    ]
