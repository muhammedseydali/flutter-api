from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from . import models
from . models import Account
from . serializers import AccountSerializer
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny


# Create your views here.

#users api_view
class AccountList(APIView):
    """
    List all Users, or create a new User.
    
    """
    serializer_class = AccountSerializer
    
    def get(self, request, format=None):
        users = models.Account.objects.all()
        serializer = AccountSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            instance=serializer.save()
            instance.set_password(instance.password)
            instance.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetail(APIView):
    
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = AccountSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = AccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = AccountSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
@csrf_exempt
def change_password(request, pk):
    if request.method == 'POST':
        password = request.POST['password']
        print(password)
        user = Account.objects.get(id=pk)
        print(user)
        user.set_password(password)
        print(user.password)
        user.save()
        return JsonResponse({'status':status.HTTP_200_OK})


from django.contrib.auth import authenticate
@csrf_exempt
def check_old_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        email = request.POST['email']
        user = authenticate(email=email, password=old_password)
        if user is not None:
            return JsonResponse({'status':True})
        else:
            return JsonResponse({'status':False})
