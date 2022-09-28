from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db import transaction

from rest_framework import generics, status, viewsets,serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView

from cars.models import Cars,CarCategory, CartItem
from accounts.models import Account, ImageType, Image
from .serializers import CarSerializer, CarCategorySerializer , CartItemSerializer
from accounts.serializers import UserDataSerializer, UserRegister, ImageSerializer, ImageTypeSerializer

from accounts.functions import get_auto_id

class CarCategoryViewset(viewsets.ModelViewSet):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            car_category = CarCategory.objects.create(
                                            **serializer.validated_data)
            car_category_data = CarCategorySerializer(car_category, many=False, context={'request': request})
            
            response_data = {
                "success": "CarCategory Successfully Created.", 
                "course_category": car_category_data.data
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)



class CarViewset(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id' 

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            cars = Cars.objects.create(
                                            **serializer.validated_data)
            car_data = CarSerializer(cars, many=False, context={'request': request})
            
            response_data = {
                "success": "Car Successfully Created.", 
                "cars": car_data
            }
            
            return Response(response_data, status=status.HTTP_201_CREATED)        




class CartItemViewset(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer