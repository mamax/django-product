# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'products/index.html', {})


def products_list(request):
    products = (
        {'id': 1,
         'name': u'Bread',
         'slug': u'Black',
         'description': u'for eating',
         'price': 235,
         'created_at': 2.12,
         'modified_at': 22.12},
        {'id': 2,
         'name': u'Meat',
         'slug': u'Red',
         'description': u'for eating',
         'price': 234,
         'created_at': 12.09,
         'modified_at': 13.09},
    )
    return render(request, 'products/products_list.html', {'products': products})


def products_add(request):
    return HttpResponse('<h1>Add Product</h1>')

def products_edit(request, gid):
    return HttpResponse('<h1>Edit product %s</h1>' % gid)
