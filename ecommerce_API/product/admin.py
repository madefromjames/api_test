from django.contrib import admin
from .models import Category, Brand, ProductImage, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    # list_per_page = 20
    ...
    

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
