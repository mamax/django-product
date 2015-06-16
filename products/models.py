# -*- coding: utf-8 -*-
from django.db import models
import datetime

# Create your models here.
class Product(models.Model):
    """Product Model"""

name = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Назва")
slug = models.SlugField(
    max_length=256,
    blank=False,
    verbose_name=u"Коротка назва-мітка")
description = models.CharField(
    max_length=256,
    blank=False,
    verbose_name=u"Опис"
    )
price = models.DecimalField(
    max_digits=5,
    decimal_places=2,
    blank=False,
    verbose_name=u"Ціна")
created_at = models.DateField(
    blank=False,
    verbose_name=u"Дата створення",
    null=True)
modified_at = models.DateField(
    blank=True,
    verbose_name=u"Дата змінення",
    default='')
