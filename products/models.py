# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Product(models.Model):
    """Product Model"""


    class Meta(object):
        verbose_name = u"Продукт"
        verbose_name_plural = u"Продукти"


    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    slug = models.SlugField(
        max_length=50,
        blank=False,
        verbose_name=u"Коротка назва-мітка")
    description = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Опис"
    )
    price = models.FloatField(
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

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.slug)
