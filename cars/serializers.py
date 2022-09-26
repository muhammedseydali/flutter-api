from operator import attrgetter
from accounts.functions import get_auto_id, to_pascal_case
from accounts.models import Image, ImageType
from .models import Cars, CarCategory, Cart, CartItem, Order
from django.db import transaction
from rest_framework import fields, serializers


class CarCategorySerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CarCategory
        fields = ['id', 'type', 'slug', 'description']



class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = ['id', 'auto_id', ' name', 'slug', 'category', 'about', 'media', 'description']



class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['id', 'car', 'user', 'date_added']


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['id', 'user', 'car', 'cart', 'quantity', 'is_active']
        
        
class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user']




