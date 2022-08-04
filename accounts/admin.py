from .models import Account
from django.contrib import admin
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('user_name', 'email', 'phone_number', 'dob', 'is_staff', 'is_admin', 'is_active') 

    filter_horizontal =()
    list_filter = ()
    fieldsets =()

# Register your models here.

admin.site.register(Account,AccountAdmin)
