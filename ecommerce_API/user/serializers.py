from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Customer
import random as r
import string as s
import re

def check_password(password):
    password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    match = re.match(password_pattern, string=password)
    return bool(match)


def validate_password(password):
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long")
    if check_password(password) == False:
        raise ValidationError("Password must contain at least one uppercase, one lowercase, one digit, and one special character")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'username', 'email', 'phone_number', 'password', 'created_at']
        
        extra_kwags = {
            'password': {'write_only': True},
            'created_at': {'read_only': True},
        }
    
    def create(self, validated_data):
        password = validated_data['password']
        if not check_password(password):
            raise ValidationError("Password must contain at least one uppercase, one lowercase, one digit, and one special character")
        
        user = Customer.objects.create(**validated_data)
        validate_password(user.password)
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get("username", instance.username)
        instance.email = validated_data.get("email", instance.email)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.save()
        return instance