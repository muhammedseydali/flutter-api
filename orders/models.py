from django.db import models

# Create your models here.
from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models
from accounts.models import Account
# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    amount_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

    class Meta:
        db_table = 'order_payment'
        verbose_name = ('payment')
        verbose_name_plural = ('payment')        

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),
    )

    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models. EmailField(max_length=50)
    address_line = models.CharField(max_length=50)
    address_line2 = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    order_total =models.FloatField()
    tax= models.FloatField()
    status = models.CharField(max_length=50, choices=STATUS, default='New')
    ip = models.CharField(max_length=50, blank=True)
    is_ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)   
    updated_at = models.DateTimeField(auto_now=True)



    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def full_address(self):
        return f'{self.address_line} {self.address_line2}'


    def __str__(self):
        return self.user.first_name

    class Meta:
        db_table = 'order_order'
        verbose_name = ('order')
        verbose_name_plural = ('order')
   

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Payment = models.ForeignKey(Payment,on_delete=models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'orders_product'
        verbose_name = ('order_product')
        verbose_name_plural = ('order_product')

    def __str__(self):
        return self.product.product_name 