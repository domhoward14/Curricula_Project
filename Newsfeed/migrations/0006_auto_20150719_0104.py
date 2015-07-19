# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0005_auto_20150719_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.CharField(default=b'Null', max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='lesson',
            field=models.CharField(default=b'Null', max_length=20, null=True),
            preserve_default=True,
        ),
    ]
