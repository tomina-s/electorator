from django.urls import path, include
<<<<<<< HEAD
from .api import CandidateViewSet, AccountPermissionsViewSet
=======
from .api import CandidateViewSet, ProtocolFirstCreate
>>>>>>> dev


<<<<<<< HEAD
# candidate_urls = [
#     path('candidate/', include('**.urls'))
# ]

# /candidate/api/...


urlpatterns = [
    # path('api/', include(candidate_urls)),

    path('list', CandidateViewSet.as_view({'get': 'list_of_candidats'})),
    # path('candidate_info/', CandidateViewSet.as_view()),  # ?? или тут view должны быть?
    # path('', include(static_url)),
    path('permission', AccountPermissionsViewSet.as_view({'get':'list_of_role_uik'})),
=======
urlpatterns = [
    path('protocols/first/', ProtocolFirstCreate.as_view()),
    path('candidates/list/', CandidateViewSet.as_view({'get': 'list_of_candidats'})),
>>>>>>> dev
]
