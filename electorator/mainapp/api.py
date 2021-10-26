from django.core import exceptions
from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Candidate, UikCandidate, Uik
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, response, status
from .serializers import (
    CandidateSerializer,
    CandidatInfoSerializer,
    ProtocolFirstSerializer,
    ProtocolSecondSerializer
)
from accounts.models import Account, Permission, Role


def get_permissions(user_id):
    try:
        perms = Permission.objects.filter(user=user_id).all()
    except Permission.DoesNotExist:  # pylint: disable=no-member
        msg = f"No permissions" \
              f" for {user_id} on uik"
        raise exceptions.PermissionDenied(msg) from Permission.DoesNotExist  # pylint: disable=no-member
    try:
        role = Role.objects.filter(user=user_id).first()
    except Permission.DoesNotExist:  # pylint: disable=no-member
        msg = f"No role" \
              f" for user {user_id}"
        raise exceptions.PermissionDenied(msg) from Role.DoesNotExist  # pylint: disable=no-member

    uik_id = 'uik_id'
    user_perms = []
    for p in perms:
        user_perms.append(getattr(p, uik_id))

    role_user = 'role_user'

    return user_perms, getattr(role, role_user)


def has_permission_for(user_id, uik, role):
    perms, user_role = get_permissions(user_id)
    return uik in perms or user_role == role


class ProtocolFirstCreate(APIView):
    """protocol api"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProtocolFirstSerializer

    def post(self, request):
        """create new first protocol"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        protocol = serializer.validated_data
        uik = protocol['num_uik']
        if not has_permission_for(request.user.id, uik, 'УИК'):
            raise exceptions.PermissionDenied()

        serializer.save()

        if protocol['sum_bul'] != 0:
            Uik.objects.filter(id=uik).update(presence=F("presence") + protocol['sum_bul'])

        return Response(status=status.HTTP_200_OK)


class ProtocolSecondCreate(APIView):
    """protocol api"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProtocolSecondSerializer

    def post(self, request):
        """create new second protocol"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        protocol = serializer.validated_data
        uik = protocol['num_uik']
        if not has_permission_for(request.user.id, uik, 'УИК'):
            raise exceptions.PermissionDenied()

        serializer.save()

        return Response(status=status.HTTP_200_OK)


class CandidateViewSet(viewsets.ModelViewSet):
    """
    ViewSet для отображения данных по кандидатам.
    Кандидат - чтение (модели).
    list_of_candidats - чтение всех кандидатов на данных выборах.
    user_list = CandidateViewSet.as_view({'get': 'list_of_candidats'})
    user_detail = CandidateViewSet.as_view({'get': '***'})
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def list_of_candidats(self, request, uik_id):
        perms, _ = get_permissions(request.user.id)
        if uik_id not in perms:
            raise exceptions.PermissionDenied

        can_ids = UikCandidate.objects.filter(id_uik=uik_id).values_list('id_candidate', flat=True)
        cans = Candidate.objects.filter(id__in=can_ids).all()

        serializer_class = CandidateSerializer(cans, many=True)
        return response.Response(serializer_class.data)

    def view_candidate_info(self, request):
        queryset = Candidate.objects.all()
        serializer_class = CandidatInfoSerializer(queryset, many=True)
        return response.Response(serializer_class.data)


class AccountPermissionsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list_of_role_uik(request):
        user = request.user
        if Account.objects.get(pk=user.id, role='ТИК') or Account.objects.get(pk=user.id, role='УИК'):
            pass
