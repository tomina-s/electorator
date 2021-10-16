from rest_framework import routers
from .api import CandidateViewSet

router = routers.DefaultRouter()
router.register('api/candidate', CandidateViewSet, 'candidate')

urlpatterns = router.urls
