from django.urls import path
from . import views

urlpatterns = [
    path('', views.Carts.as_view(), name='carts'),
]