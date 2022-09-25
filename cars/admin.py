from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cars, CarCategory


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
      
