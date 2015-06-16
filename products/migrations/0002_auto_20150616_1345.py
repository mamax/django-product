# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='modified_at',
            field=models.DateField(default=b'', verbose_name='\u0414\u0430\u0442\u0430 \u0437\u043c\u0456\u043d\u0435\u043d\u043d\u044f', blank=True),
        ),
    ]
