# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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

    # paginate students
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/products_list.html', {'products': products})


def products_add(request):
    return HttpResponse('<h1>Add Product</h1>')

def products_edit(request, gid):
    return HttpResponse('<h1>Edit product %s</h1>' % gid)
