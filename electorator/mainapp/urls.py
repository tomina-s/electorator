from django.urls import path, include
from .api import (
    CandidateViewSet,
    ProtocolFirstCreate,
    ProtocolSecondCreate,
    AccountPermissionsViewSet, PresenceViewSet,
)

urlpatterns = [
    path('protocols/first/', ProtocolFirstCreate.as_view()),

    path('protocols/second/', ProtocolSecondCreate.as_view()),
    path('uik/<int:uik_id>/candidates/short/list/', CandidateViewSet.as_view({'get': 'list_of_candidats'})),

    path('accounts/permission/', AccountPermissionsViewSet.as_view({'get':'list_of_role_uik'})),
    path('presence/',PresenceViewSet.as_view())
]
