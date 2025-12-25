from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('category/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),

]
