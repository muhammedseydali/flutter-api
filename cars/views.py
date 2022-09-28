from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.http.response import Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics, status, viewsets,serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, parser_classes,authentication_classes,permission_classes


from cars.models import Cars,CarCategory, CartItem
from accounts.models import Account, ImageType, Image
from .serializers import CarSerializer, CarCategorySerializer , CartItemSerializer
from accounts.serializers import UserDataSerializer, UserRegister, ImageSerializer, ImageTypeSerializer


class CarViewset(ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'

    def get_serializer_context(self):
        return {
            'request': self.request,
            'user': self.request.user
        }



class CarCategoryViewset(viewsets.ModelViewSet):
    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer  

class CartItemViewset(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer