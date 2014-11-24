# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vsuser',
            name='thirdPartAccessToken',
            field=models.CharField(max_length=400, null=True),
            preserve_default=True,
        ),
    ]
