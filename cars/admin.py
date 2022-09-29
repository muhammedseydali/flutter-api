from ast import Mod
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cars, CarCategory, Cart, CartItem


class CarCategoryAdmin(admin.ModelAdmin):
    model = CarCategory
    list_display = ('id', 'type', 'slug', 'description') 
    prepopulated_fields = {'slug':('type',)}
    filter_horizontal = ()
    list_filter = ()
admin.site.register(CarCategory, CarCategoryAdmin)  


class CarAdmin(admin.ModelAdmin):
    model = Cars
    list_display = ('id', 'name', 'slug', 'category', 'description', 'about', 'media') 
    prepopulated_fields = {'slug':('name',)}
    filter_horizontal = ()
    list_filter = ()
admin.site.register(Cars, CarAdmin)  

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = ('id', 'car', 'user', 'date_added')
    filter_horizontal = ()
    list_filter = ()
admin.site.register(Cart, CartAdmin) 

class CarItemAdmin(admin.ModelAdmin):
    model = CartItem
    list_display = ('id', 'user', 'car', 'cart', 'quantity', 'is_active')
    filter_horizontal = ()
    list_filter = ()
admin.site.register(CartItem, CarItemAdmin) 


      
