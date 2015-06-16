# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, verbose_name='\u0406\u043c\u044f')),
                ('slug', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('description', models.CharField(max_length=256, verbose_name='\u041f\u0440\u0456\u0437\u0432\u0438\u0449\u0435')),
                ('price', models.DecimalField(max_digits=5, decimal_places=2, verbose_name='\u0411\u0456\u043b\u0435\u0442')),
                ('created_at', models.DateField(verbose_name='\u0414\u0430\u0442\u0430\u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f')),
                ('modified_at', models.DateField(verbose_name='\u0414\u0430\u0442\u0430\u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

