# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0004_comment_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='lesson',
        ),
    ]
