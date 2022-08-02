from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)

urlpatterns = [
    #login
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    