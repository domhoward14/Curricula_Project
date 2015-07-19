# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0002_remove_comment_parentid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='professor',
        ),
    ]
