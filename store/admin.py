from django.contrib import admin
# username :- SamikshaGulhane
# email :- gulhanesamiksha020@gmail.com
#password :- ecommers
# Register your models here.
from .models import Category, Product

admin.site.register(Category)
admin.site.register(Product)

