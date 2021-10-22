from rest_framework import routers
from django.urls import path, include
from .api import CandidateViewSet

# router = routers.DefaultRouter()
# router.register('api/candidate', CandidateViewSet, 'candidate')
#
# urlpatterns = router.urls

# candidate_urls = [
#     path('candidate/', include('**.urls'))  # TODO **
# ]

# /candidate/api/...
urlpatterns = [
    # path('api/', include(candidate_urls)),

    path('list/', CandidateViewSet.as_view({'get': 'list_of_candidats'})),
    # path('candidate_info/', CandidateViewSet.as_view()),  # ?? или тут view должны быть?
    # path('', include(static_url)),

]