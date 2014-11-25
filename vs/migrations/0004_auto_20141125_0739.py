# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vs', '0003_auto_20141125_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placevideo',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='placevideo',
            name='url',
        ),
        migrations.AddField(
            model_name='placevideo',
            name='video',
            field=models.ForeignKey(default='', to='vs.Video'),
            preserve_default=False,
        ),
    ]
