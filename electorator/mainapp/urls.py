from rest_framework import routers
from django.urls import path, include
from .api import CandidateViewSet

router = routers.DefaultRouter()
router.register('api/candidate', CandidateViewSet, 'candidate')

urlpatterns = router.urls

candidate_urls = [
    path('candidate/', include('**.urls'))  # TODO **
]

# /candidate/api/...
urlpatterns = [
    path('api/', include(candidate_urls)),

    path('candidats_list/', CandidateViewSet.list_of_candidats),
    path('candidate_info/', CandidateViewSet.view_candidate_info), # ?? или тут view должны быть?
    # path('', include(static_url)),

]

