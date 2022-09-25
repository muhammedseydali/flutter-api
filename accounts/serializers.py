from operator import attrgetter
from .functions import get_auto_id, to_pascal_case
from .models import Account, Image, ImageType
from django.db import transaction
from rest_framework import fields, serializers


class ImageTypeSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ImageType
        fields = ['id', 'auto_id', 'type', 'value']

    def create(self, validated_data):
        creator = self.context['Account']
        auto_id = get_auto_id(ImageType)
        return ImageType.objects.create(creator=creator, auto_id=auto_id, **validated_data)


class ImageSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    model_name = serializers.CharField(read_only=True)
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = [ 'id', 'auto_id', 'name', 'model_name', 'reference_id', 'image_type', 'image', 'description']
      
    def validate_model_name(self, value):
        if to_pascal_case(value) in map(attrgetter('__name__'), apps.get_models()):
            return to_pascal_case(value)
        raise serializers.ValidationError("Couldn't find model class for %s" % to_pascal_case(value)) 
                
    def create(self, validated_data):
        creator = self.context['Account']
        auto_id = get_auto_id(Image)
        return Image.objects.create(creator=creator, auto_id=auto_id, **validated_data)
    
    
class ProgramImageSerializer(serializers.ModelSerializer):
    auto_id = serializers.IntegerField(read_only=True)
    model_name = serializers.CharField(read_only=True)
    reference_id = serializers.UUIDField(read_only=True)
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)


    class Meta:
        model = Image
        fields = ['id', 'auto_id', 'name', 'model_name', 'reference_id', 'image_type', 'image', 'description']

    def get_image(self, instance):
        request = self.context['request']
        image_url = instance.image.image.url
        return request.build_absolute_uri(image_url)

    
    
class UserRegister(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    profile_picture = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = Account
        fields = ['id','username','phone_number','email','dob','profile_picture','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }
    
    
    def save(self):
        with transaction.atomic():
            reg = Account(
                email=self.validated_data['email'],
                phone_number=self.validated_data['phone_number'],
                dob=self.validated_data['dob'],
                username=self.validated_data['username'],
                profile_picture=self.validated_data['profile_picture'],
            )
            if Account.objects.filter(phone_number=self.validated_data['phone_number']).exists():
                raise serializers.ValidationError({'error':'phone number already registered!!'})
            password=self.validated_data['password']
            password2=self.validated_data['password2']
            
            if password != password2:
                raise serializers.ValidationError({'error':'password does not match!!'})
            reg.set_password(password)
            reg.save()
        return reg
 
 
    
class UserDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Account
        fields=['id','username','phone_number','email','dob','profile_picture']