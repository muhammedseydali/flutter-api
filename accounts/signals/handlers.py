# from django.dispatch import receiver
# from django.db.models.signals import pre_save
# from accounts.functions import unique_slug_generator


# @receiver(pre_save, sender=Language)
# def pre_save_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#        instance.slug = unique_slug_generator(instance)
