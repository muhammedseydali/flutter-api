from .models import Account, Image, ImageType
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .functions import get_auto_id
# Register your models here.


class AccountAdmin(BaseUserAdmin):
    model = Account
    list_display = ('username', 'email', 'phone_number', 'dob', 'is_staff', 'is_admin', 'is_active') 

    filter_horizontal =()
    list_filter = ()
    fieldsets =()


class ImageTypeAdmin(admin.ModelAdmin):
    model = ImageType
    list_display = ('id', 'type', 'value') 
   

class ImageAdmin(admin.ModelAdmin):
    model = Image
    list_display = ('id', 'name', 'image', 'model_name', 'reference_id')

admin.site.register(Account,AccountAdmin)
admin.site.register(ImageType, ImageTypeAdmin)  
admin.site.register(Image, ImageAdmin) 


