from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Product , Category
from django.contrib import messages

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })

# vew displayed products by category
def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)

    return render(request, 'store/home.html', {
        'products': products,
        'categories': Category.objects.all()
    })

# view for specific product details

from django.shortcuts import get_object_or_404

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    messages.success(request, "Product added to cart successfully!")
    return redirect('home')


def cart(request):
    cart = request.session.get('cart', {})
    products = []
    total = 0

    for pid, qty in cart.items():
        product = Product.objects.get(id=pid)
        product.qty = qty
        product.subtotal = product.price * qty
        total += product.subtotal
        products.append(product)

    return render(request, 'store/cart.html', {
        'products': products,
        'total': total
    })


