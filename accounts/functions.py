import string, random, requests
import uuid
from django.apps import apps
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save

def get_file_path(instance, filename):
    
    extension = filename.split(".")[-1]

    instance_slug = getattr(instance,"slug",False)
    if not instance_slug:
        instance_slug = str(uuid.uuid4()).replace("-","")

    return "uploads/{0}s/{1}/{2}/{3}" . format (instance._meta.model_name, instance._meta.app_label, instance.image_type, filename)       

#convert normal text to pascal case
def to_pascal_case(value):
    return "".join(value.title().split())

#slug auto generation
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None, post=False):
    if new_slug is not None:
        slug = slugify(new_slug)
    else:
        try:
            if instance.title:
                slug = slugify(instance.title.lower())
        except:
            slug = slugify(instance.name.lower())    

def get_auto_id(model):
    auto_id = 1
    if model.objects.filter(auto_id=auto_id).exists():
        latest_auto_id = model.objects.latest("auto_id").auto_id
        if latest_auto_id:
            auto_id = latest_auto_id + 1
    return auto_id
