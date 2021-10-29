from django.urls import path, include
from .api import (
    CandidateViewSet,
    ProtocolFirstCreate,
    ProtocolSecondCreate,
    AccountPermissionsViewSet, PresenceViewSet, PercVotersViewSet, TopPresenceViewSet, TopTikViewSet,
    GeneralInfoViewSet,
)

urlpatterns = [
    path('protocols/first/', ProtocolFirstCreate.as_view()),

    path('protocols/second/', ProtocolSecondCreate.as_view()),
    path('uik/<int:uik_id>/candidates/short/list/', CandidateViewSet.as_view({'get': 'list_of_candidats'})),

    path('accounts/permission/', AccountPermissionsViewSet.as_view({'get': 'list_of_role_uik'})),
    path('presence/', PresenceViewSet.as_view()),
    path('votes/', PercVotersViewSet.as_view()),
    path('toppresence/', TopPresenceViewSet.as_view()),
    path('toptik/', TopTikViewSet.as_view()),
    path('generalinfo/', GeneralInfoViewSet.as_view())
]
