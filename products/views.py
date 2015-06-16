# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'products/index.html', {})


def products_list(request):
    products = Product.objects.all()

    # try to order products list
    order_by = request.GET.get('order_by', '')
    if order_by in ('first_name', 'description', 'price'):
        products = products.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            products = products.reverse()

    return render(request, 'products/products_list.html', {'products': products})


def products_add(request):
    return HttpResponse('<h1>Add Product</h1>')

def products_edit(request, gid):
    return HttpResponse('<h1>Edit product %s</h1>' % gid)
