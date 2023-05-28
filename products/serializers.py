from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CartItem
from django.http import JsonResponse

from products.models import Food, Order

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


#Food Serializer

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['title', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title']
