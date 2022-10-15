from django.db import models
from accounts.models import Account

from accounts.functions import get_auto_id
# Create your models here.

class CarCategory(models.Model):

    CAR_TYPE =[

        ('HATCHBACK', 'Hatchback'),
        ('SEDAN', 'Sedan'),
        ('SUV', 'Suv')
    ]
    type = models.CharField(max_length=255, choices=CAR_TYPE, default='SEDAN')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(max_length=255, blank=True)

    class Meta:
        db_table = 'car_category'
        verbose_name = ('car_category')
        verbose_name_plural = ('car_category')
        ordering = ('id',)

    def __str__(self):
        return self.type

class Cars(models.Model):

    name = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=255, blank=True)
    category = models.OneToOneField('cars.CarCategory', on_delete=models.CASCADE, related_name="categories")
    about = models.TextField()
    media = models.URLField()
    description = models.TextField()

    class Meta:
        db_table = 'cars_cars'
        verbose_name = ('cars')
        verbose_name_plural = ('cars')

    def __str__(self):
        return self.name

        
class Cart(models.Model):
    car = models.ForeignKey('cars.Cars', on_delete=models.CASCADE, related_name="cars")
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name="accounts")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'car={0}'.format(self.car)

class CartItem(models.Model):
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, null=True)
    car = models.ForeignKey('cars.Cars', on_delete= models.CASCADE)
    cart = models.ForeignKey('cars.Cart', on_delete= models.CASCADE)
    quantity = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.car.price * self.quantity

    def __unicode__(self):
        return self.product

    def __str__(self):
        return self.cart

class Order(models.Model):
    user = models.ForeignKey('accounts.Account', on_delete=models.CASCADE, related_name="orders")

    def __str__(self):
        return self.user