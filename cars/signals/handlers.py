from django.dispatch import receiver
from django.db.models.signals import pre_save
from cars.models import CarCategory, Car
from cars.functions import unique_slug_generator
from cars.models import Cars,CarCategory,CartItem

