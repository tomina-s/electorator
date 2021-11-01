from django.urls import path, include
from .api import (
    CandidateViewSet,

    ProtocolsFirstList,
    ProtocolsFirstListQuantity,
    ProtocolFirst,

    ProtocolSecondCreate,
    AccountPermissionsViewSet, PresenceViewSet, TopPresenceViewSet, TopTikViewSet,
    GeneralInfoViewSet,
    UikAvailableList,
    UikAvailableQuantity, GeneralInfoPresenceViewSet, VotesPresenceViewSet, Top24PresenceViewSet,
    CandidateDescVotesViewSet

)

urlpatterns = [
    path('protocols/first/', ProtocolFirst.as_view()),
    path('protocols/first/<int:prot_id>', ProtocolFirst.as_view()),


    path('protocols/second/', ProtocolSecondCreate.as_view()),
    path('uiks/available/list/<int:page>/', UikAvailableList.as_view()),
    path('uiks/available/quantity/', UikAvailableQuantity.as_view()),

    path('uiks/candidates/short/list/', CandidateViewSet.as_view()),
    path('uiks/candidates/short/list/desc/',CandidateDescVotesViewSet.as_view()),
    path('uiks/<int:uik_id>/protocols/first/list/<int:page>/', ProtocolsFirstList.as_view()),
    path('uiks/<int:uik_id>/protocols/first/quantity/', ProtocolsFirstListQuantity.as_view()),
    path('protocols/second/', ProtocolSecondCreate.as_view()),

    path('accounts/permission/', AccountPermissionsViewSet.as_view({'get': 'list_of_role_uik'})),
    path('presence/', PresenceViewSet.as_view()),
    #path('votes/', PercVotersViewSet.as_view()),
    path('toppresence/', TopPresenceViewSet.as_view()),
    path('top24presence/', Top24PresenceViewSet.as_view()),
    path('toptik/', TopTikViewSet.as_view()),
    path('generalinfo/', GeneralInfoViewSet.as_view()),
    path('generalinfopresence/', GeneralInfoPresenceViewSet.as_view()),
    path('votespresence/',VotesPresenceViewSet.as_view())



]
