# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.IntegerField(choices=[(1, b'like'), (2, b'comments'), (3, b'view')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='placevideo',
            name='place',
            field=models.ForeignKey(related_name='placeVideos', to='vs.Place'),
            preserve_default=True,
        ),
    ]
