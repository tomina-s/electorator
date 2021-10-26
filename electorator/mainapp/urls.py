from django.urls import path, include
from .api import CandidateViewSet, ProtocolFirstCreate


urlpatterns = [
    path('protocols/first/', ProtocolFirstCreate.as_view()),
    path('candidates/list/', CandidateViewSet.as_view({'get': 'list_of_candidats'})),
]
