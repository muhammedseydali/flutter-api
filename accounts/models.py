from .functions import get_file_path
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,username,phone_number,email,dob,profile_picture,password=None):
            if not email:
                raise ValueError('Email Address Is Mandatory')
            
            user = self.model(
                email = self.normalize_email(email),
                username = username,
                phone_number = phone_number,
                dob = dob,
                profile_picture = profile_picture     
            )
            user.set_password(password)
            user.save(using = self._db) 
            return user 
        
    def create_superuser(self,username,phone_number,email,dob,profile_picture,password):
            user = self.create_user(
                email = self.normalize_email(email),
                username=username,
                phone_number=phone_number,
                password=password,
                dob = dob,
                profile_picture = profile_picture
            ) 
            user.is_admin = True
            user.is_active = True
            user.is_staff = True
            user.is_superadmin = True
            user.save(using=self._db)
            return user   

class Account(AbstractBaseUser):
    username = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15,unique=False,blank=True)
    email = models.EmailField(max_length=100,unique=True)
    dob = models.DateField()
    profile_picture = models.ImageField(upload_to='images/',null=True)
    password = models.CharField(max_length=255)
    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','phone_number','dob','profile_picture']
    
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True


class ImageType(models.Model):
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    creator = models.ForeignKey('Account', on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    value = models.PositiveIntegerField()
    
    class Meta:
        db_table = 'general_image_type'
        verbose_name = _('image_type')
        verbose_name_plural = _('image_types')
        ordering = ('type',)

    def __str__(self):
        return self.type
    
    
class Image(models.Model):
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    creator = models.ForeignKey('Account', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    reference_id = models.UUIDField()
    image_type = models.ForeignKey("ImageType", related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'general_image'
        verbose_name = _('image')
        verbose_name_plural = _('images')
        ordering = ('name',)

    def __str__(self):
        return self.name

