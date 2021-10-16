from .models import Candidate
from rest_framework import viewsets, permissions
from .serializers import CandidateSerializer
# мб еще импорты по сералайзеру должны быть и другие классы из сериалайзера


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CandidateSerializer
