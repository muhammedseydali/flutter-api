from django.urls import path, include,re_path

from rest_framework.routers import DefaultRouter
from rest_framework import routers

from .import views


router = routers.DefaultRouter()

router.register(r'cars', views.CarViewset)
router.register(r'CarCategory', views.CarCategoryViewset)
router.register(r'CartItem', views.CartItemViewset)

urlpatterns = [
    path(r'', include(router.urls)),
]