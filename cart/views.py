from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from .models import Cart, CartItem  
from rest_framework.response import Response
from django.http import Http404
from .serializers import *

# Create your views here.
# class CartViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializers_class = CreateCartSerializer
#     queryset = CartItem

class Carts(APIView):
    def get(self, request):
        obj = Cart.objects.all()
        serializers = CartSerializer(obj, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializers = CartSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

