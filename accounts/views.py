from .models import Account


from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.http.response import Http404
from django.shortcuts import render
from .serializers import UserDataSerializer, UserRegister
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, parser_classes,authentication_classes,permission_classes

# Create your views here.


class RegistersViews(generics.CreateAPIView):

    serializer_class = UserRegister
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "data": UserRegister(user,context=self.get_serializer_context()).data,
            "message": "Registered Successfully.  Now perform Login to get your token",
        })


class UsersLists(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request):
        user = Account.objects.all()
        serializer = UserDataSerializer(user,many=True)
        return Response(serializer.data)


class UserDetails(APIView):
    permission_classes = [IsAdminUser]
    def get(self,request,pk):
        id = pk
        user = Account.objects.get(pk=id)
        serializer = UserDataSerializer(user)
        return Response(serializer.data)
    
    
    def put(self,request,pk):
        id = pk
        user = Account.objects.get(pk=id)
        serializer = UserDataSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'data updated successfully'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request,pk):
        id = pk
        user = Account.objects.get(pk=id)
        user.delete()
        return Response({'message':'user deleted'})
    