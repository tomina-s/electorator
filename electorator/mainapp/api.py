from django.core import exceptions
from django.db.models import F
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Candidate, UikCandidate, Uik, Protocol1
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
    return (uik in perms and user_role == role) or user_role == "ЦИК"


class ProtocolFirst(APIView):
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
        if protocol['bad_form'] != 0:
            Uik.objects.filter(id=uik).update(bad_form=F("bad_form") + protocol['bad_form'])

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def get(request, prot_id):
        protocol = Protocol1.objects.filter(id=prot_id).first()
        num_uik = protocol.num_uik
        perms, role = get_permissions(request.user.id)
        if num_uik not in perms and role != "ЦИК":
            raise exceptions.PermissionDenied()

        protocol = Protocol1.objects.filter(id=prot_id).first()
        serializer_class = ProtocolFirstSerializer(protocol)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class ProtocolsFirstList(APIView):
    """protocol api"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProtocolFirstSerializer

    def get(self, request, uik_id):
        """get list of the first protocols"""
        page = int(request.GET.get('page', 1))
        perm, role = get_permissions(request.user.id)
        if uik_id not in perm and role != "ЦИК":
            raise exceptions.PermissionDenied()

        protocols = Protocol1.objects.filter(num_uik=uik_id).order_by('-id')[(page - 1) * 10:page * 10]
        serializer_class = ProtocolFirstSerializer(protocols, many=True)

        return Response(serializer_class.data, status=status.HTTP_200_OK)


class ProtocolsFirstListQuantity(APIView):
    """protocol api"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, uik_id):
        """get countity of the first protocols"""
        perm, role = get_permissions(request.user.id)
        if uik_id not in perm and role != "ЦИК":
            raise exceptions.PermissionDenied()

        quantity = Protocol1.objects.filter(num_uik=uik_id).count()

        return Response({
            'quantity': quantity
        }, status=status.HTTP_200_OK)


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
    permission_classes = [IsAuthenticated]

    @staticmethod
    def list_of_role_uik(request):
        user = request.user
        if Account.objects.get(pk=user.id, role='ТИК') or Account.objects.get(pk=user.id, role='УИК'):
            pass
