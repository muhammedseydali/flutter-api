from django.dispatch import receiver
from django.db.models.signals import pre_save
from cars.models import CarCategory, Car
from cars.functions import unique_slug_generator
from cars.models import Cars,CarCategory,CartItem


@receiver(pre_save, sender=Cars)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
       instance.slug = unique_slug_generator(instance)

@receiver(pre_save, sender=CarCategory)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
       instance.slug = unique_slug_generator(instance)