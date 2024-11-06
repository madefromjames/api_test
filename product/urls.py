from django.urls import path
from . import views

urlpatterns = [
    path('', views.Products.as_view(), name='products'),
    path('<str:id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('<str:query>/', views.ProductSearch.as_view(), name='product_search'),
    path('categories/', views.CategoryView.as_view(), name='all-categories'),
    path('brands/', views.BrandView.as_view(), name='all-brands'),
    path('sort/category/<int:pk>', views.ProductByCategory.as_view(), name='sort-by-category'),
    path('sort/brand/<int:pk>', views.ProoductBrand.as_view(), name='product-count'),
    path('count/', views.ProductCount.as_view(), name='product-count'),
]