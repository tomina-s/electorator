from .models import Candidate, Uik, Protocol2
from accounts.models import Account, Permission, Role
from rest_framework import viewsets, permissions, response
from .serializers import CandidateSerializer, CandidatInfoSerializer, RoleSerializer, UikSerializer, PresenceSerializer, \
    VotesSerializer
from rest_framework.decorators import action

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
from django.db.models import Sum, Count


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

        Uik.objects.filter(id=uik).update(status=protocol['status'])
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

        Candidate.objects.filter(id=protocol['name'].id) \
            .update(sum_votes=F("sum_votes") + protocol['candidate_votes'])

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
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def list_of_role_uik(self, request):
        user = request.user
        user_role = Role.objects.get(user_id=user.id)
        role = RoleSerializer(user_role)
        new_dict = {}
        new_dict.update(role.data)
        if user_role.role_user == 'ВИК':
            return response.Response(new_dict)
        user_uik = Permission.objects.get(user_id=user.id)
        num_uik = Uik.objects.get(pk=user_uik.uik_id)
        uik = UikSerializer(num_uik)
        new_dict.update(uik.data)
        return response.Response(new_dict)


class PresenceViewSet(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        queryset = Uik.objects.values('num_tik').annotate(presence=Sum('presence'))
        serializer_class = PresenceSerializer(queryset, many=True)
        serializer_class.is_valid(raise_exception=True)
        return response.Response(serializer_class.data)


class PercVotersViewSet(APIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):
        sum_votes = Uik.objects.aggregate(Sum('sum_votes'))
        a = sum_votes['sum_votes__sum']
        queryset = Candidate.objects.all()
        serializer_class = VotesSerializer(queryset, many=True)
        for el in serializer_class.data:
            el['sum_votes'] = f"{round((el['sum_votes']/a)*100,1)}%"
        return response.Response(serializer_class.data)


#class TopPresence(APIView):
#    permission_classes = [
#        permissions.IsAuthenticated
#    ]
