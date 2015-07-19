# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0003_remove_comment_professor'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='professor',
            field=models.CharField(default=b'Null', max_length=20, null=True),
            preserve_default=True,
        ),
    ]
