# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vs', '0004_auto_20141125_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placevideo',
            name='location',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='placevideo',
            name='thumbnail',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
