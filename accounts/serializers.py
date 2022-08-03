from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Account
        fields=['id', 'email', 'username', 'bio', 'mobile', 'dp','is_active','is_superuser','last_login','joined_date']
        extra_kwargs = {'username': {'required': False},'email': {'required': False}}

 