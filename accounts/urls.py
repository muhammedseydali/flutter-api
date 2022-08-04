from django.urls import path
from django.conf.urls import include
from.views import RegisterView,RegistersViews, UserDetails, UsersLists,getView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





urlpatterns = [

<<<<<<< HEAD
   path('register/',RegisterView.as_view(),name='register'),
   path('registers/',RegistersViews.as_view(),name='registers'),
   
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   
   path('UsersLists/',UsersLists.as_view(),name="UsersLists"),
   path('userDetails/<int:pk>/',UserDetails.as_view(),name="userDetails"),
=======
    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> b03c6c272e36e45ec0abab576921fa614665df98

   path('all',getView.as_view(),name='get')
   
   
]
