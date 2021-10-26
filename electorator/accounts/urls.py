"""urls for account API"""
from django.urls import re_path

from .views import Login, Permissions, Roles

urlpatterns = [
    re_path('accounts/', Login.as_view(), name='user_login'),
    re_path('permissions/', Permissions.as_view(), name='permissions'),
    re_path('roles/', Roles.as_view(), name='roles'),
]
