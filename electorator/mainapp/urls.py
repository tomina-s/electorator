from django.urls import path, include

from .api import CandidateViewSet, AccountPermissionsViewSet

from .api import CandidateViewSet, ProtocolFirstCreate




# candidate_urls = [
#     path('candidate/', include('**.urls'))
# ]

# /candidate/api/...




urlpatterns = [
    path('protocols/first/', ProtocolFirstCreate.as_view()),
    path('candidates/list/', CandidateViewSet.as_view({'get': 'list_of_candidats'})),
    path('account/permission/', AccountPermissionsViewSet.as_view({'get': 'list_of_role_uik'})),

]
