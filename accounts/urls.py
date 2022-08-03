from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework import permissions
# from swagger import schema_view


admin.site.site_header = 'Administrator Dashboard'
admin.site.site_title = "Rince Admin"
admin.site.index_title = 'Admin'

urlpatterns = [
    #login
    
    path('users_list', views.AccountList.as_view()),
    path('user_details/<int:pk>/', views.AccountDetail.as_view()),
    path('change_password/<int:pk>/', views.change_password),
    path('check_old_password', views.check_old_password),

    # re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

