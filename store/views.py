from django.shortcuts import render
from django.http import HttpResponse
from .models import Product , Category


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })

# vew displayed products by category
def category_products(request,cat_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=cat_id)
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })

# view for specific product details

from django.shortcuts import get_object_or_404

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})


