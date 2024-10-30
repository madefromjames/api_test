from django.contrib import admin
from .models import Category, Brand, ProductImage, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'quantity', 'brand', 'price', 'date_added']
    search_fields = ('name', 'description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profile_image']
    search_fields = ['name']

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
