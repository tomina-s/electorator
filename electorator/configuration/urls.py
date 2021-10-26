"""urls for account API"""
from django.urls import re_path

from .views import ConfigAPIView

urlpatterns = [
    re_path('', ConfigAPIView.as_view(), name='config'),
]
