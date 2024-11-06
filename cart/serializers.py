from rest_framework import serializers
from .models import *

"""GET Serializer"""

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']

class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']

"""POST Serializer"""

class CreateCartSerializer(serializers.ModelSerializer):
    cart = serializers.SlugRelatedField(slug_field='id', queryset=Cart.objects.all())
    product = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all())

    class Meta:
        model = CartItem
        fields = ['cart', 'product', 'quantity']

    def create(self, validated_data):
        return CartItem.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        return instance