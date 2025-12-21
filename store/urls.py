from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:cat_id>/', views.category_products, name='category_products'),
    path('product/<int:id>/', views.product_details, name='product_detail'),
]
