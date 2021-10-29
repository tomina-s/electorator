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
    ProtocolSecondSerializer, UIKSerializer
)
from accounts.models import Account, Permission, Role


def get_permissions(user_id):
    """Поулчить роль и доступы пользователя по id"""
    try:
        perms = Permission.objects.filter(user=user_id).all().values_list('uik', flat=True)
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

    return list(perms), role.role_user


def has_permission_for(user_id, uik, role):
    """Првоерить, есть ли у пользователя доступ к УИК"""
    perms, user_role = get_permissions(user_id)
    return (uik in perms and user_role == role) or user_role == "ЦИК"


class ProtocolFirst(APIView):
    """Создать и получить протокол"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProtocolFirstSerializer

    def post(self, request):
        """Создать новый протокол первого типа"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        protocol = serializer.validated_data
        uik = protocol['num_uik']
        if not has_permission_for(request.user.id, uik.id, 'УИК'):
            raise exceptions.PermissionDenied()

        inner_num = Protocol1.objects.filter(num_uik=uik.id).count() + 1
        serializer.validated_data['num_protocol_1'] = inner_num

        serializer.is_valid(raise_exception=True)
        serializer.save()

        Uik.objects.filter(id=uik.id).update(status=protocol['status'])
        if protocol['sum_bul'] != 0:
            Uik.objects.filter(id=uik.id).update(presence=F("presence") + protocol['sum_bul'])
        if protocol['bad_form'] != 0:
            Uik.objects.filter(id=uik.id).update(bad_form=F("bad_form") + protocol['bad_form'])

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def get(request, prot_id):
        """Получить протокол по id"""
        protocol = Protocol1.objects.filter(id=prot_id).first()
        num_uik = protocol.num_uik
        perms, role = get_permissions(request.user.id)
        if num_uik not in perms and role != "ЦИК":
            raise exceptions.PermissionDenied()

        protocol = Protocol1.objects.filter(id=prot_id).first()
        serializer_class = ProtocolFirstSerializer(protocol)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


class ProtocolsFirstList(APIView):
    """Список протоколов 1 типа с пагинацией"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProtocolFirstSerializer

    @staticmethod
    def get(request, uik_id, page):
        """Все протоколы с данного участка"""
        perm, role = get_permissions(request.user.id)
        if uik_id not in perm and role != "ЦИК":
            raise exceptions.PermissionDenied()

        protocols = Protocol1.objects.filter(num_uik=uik_id).order_by('-id')[(page - 1) * 10:page * 10]
        serializer_class = ProtocolFirstSerializer(protocols, many=True)

        return Response(serializer_class.data, status=status.HTTP_200_OK)


class ProtocolsFirstListQuantity(APIView):
    """Количество протоколов на участке для пагинации"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, uik_id):
        """Количество протоколов"""
        perm, role = get_permissions(request.user.id)
        if uik_id not in perm and role != "ЦИК":
            raise exceptions.PermissionDenied()

        quantity = Protocol1.objects.filter(num_uik=uik_id).count()

        return Response({
            'quantity': quantity
        }, status=status.HTTP_200_OK)


class UikAvailableList(APIView):
    """uik api"""
    permission_classes = [IsAuthenticated]
    serializer_class = UIKSerializer

    def get(self, request, page):
        """get list of the first protocols"""
        perm, role = get_permissions(request.user.id)
        if role == "ЦИК":
            uiks = Uik.objects.order_by('id')[(page - 1) * 10:page * 10]
        else:
            uiks = Uik.objects.filter(id__in=perm).order_by('id')[(page - 1) * 10:page * 10]

        serializer_class = UIKSerializer(uiks, many=True)

        return Response(serializer_class.data, status=status.HTTP_200_OK)


class UikAvailableQuantity(APIView):
    """uik api"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Получить количество доступных УИК"""
        perm, role = get_permissions(request.user.id)
        quantity = len(perm)
        if role == "ЦИК":
            quantity = Uik.objects.count()

        return Response({
            'quantity': quantity,
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
        if not has_permission_for(request.user.id, uik.id, 'УИК'):
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
