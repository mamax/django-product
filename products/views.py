from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'products/index.html', {})

def products_list(request):
    return render(request, 'products/products_list.html', {})
