from rest_framework import routers
from django.urls import path, include
from .api import CandidateViewSet

# router = routers.DefaultRouter()
# router.register('api/candidate', CandidateViewSet, 'candidate')
#
# urlpatterns = router.urls

candidate_urls = [
    path('candidate/', include('**.urls'))  # TODO **
]
# candidate_list = CandidateViewSet.as_view({'get': 'list'})
# candidate_detail = CandidateViewSet.as_view({'get': 'retrieve'})
# /candidate/api/...
urlpatterns = {

    path('api/', include(candidate_urls)),

    path('candidats_list/', CandidateViewSet.as_view({'get': 'list'}))


    # path('candidate_info/', CandidateViewSet.view_candidate_info.as_view()), # ?? или тут view должны быть?
    # path('', include(static_url)),

}

