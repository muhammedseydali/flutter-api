from django.urls import path
from django.conf.urls import include
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

   path('register/',views.RegistersViews.as_view(),name='registers'),
   
   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('UsersLists/',views.UsersLists.as_view(),name="UsersLists"),
   path('userDetails/<int:pk>/',views.UserDetails.as_view(),name="userDetails"),

   
]
