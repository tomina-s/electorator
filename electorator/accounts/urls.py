"""urls for account API"""
from django.urls import re_path

from .views import LoginAPIView

urlpatterns = [
    re_path(r'^login/?$', LoginAPIView.as_view(), name='user_login'),
]
