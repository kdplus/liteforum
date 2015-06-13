# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_post_click_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='vedio_count',
            field=models.IntegerField(default=0),
        ),
    ]
