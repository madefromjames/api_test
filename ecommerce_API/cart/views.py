from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from .models import Cart, CartItem  
from rest_framework.response import Response
from django.http import Http404
from .serializers import *

# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializers_class = CreateCartSerializer
    queryset = CartItem