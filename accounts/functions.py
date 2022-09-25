from operator import imod
import uuid
from django.apps import apps

def get_file_path(instance, filename):
    
    extension = filename.split(".")[-1]

    instance_slug = getattr(instance,"slug",False)
    if not instance_slug:
        instance_slug = str(uuid.uuid4()).replace("-","")

    return "uploads/{0}s/{1}/{2}/{3}" . format (instance._meta.model_name, instance._meta.app_label, instance.image_type, filename)       