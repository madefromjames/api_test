from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        return instance

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'profile_image']
        read_only_fields = ['id']

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.profile_image = validated_data.get("profile_image", instance.profile_image)
        
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['images']

    def create(self, validated_data):
        return ProductImage.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.images = validated_data.get("images", instance.images)
        return instance

class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(slug_field='name', queryset=Brand.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity', 'brand', 'category', 'product_image']

    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.price = validated_data.get("price", instance.price)
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.brand = validated_data.get("brand", instance.brand)
        instance.category = validated_data.get("category", instance.category)
        instance.product_image = validated_data.get("product_image", instance.product_image)
        return instance