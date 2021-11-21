"""Main app API"""
from django.core import exceptions
from django.db.models import Sum, Count, F
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, response, status

from accounts.models import Permission, Role
from .models import Protocol2, Tik, Candidate, Uik, Protocol1
from .serializers import RoleSerializer, UikSerializer, PresenceSerializer, \
    VotesSerializer, TopTikSerializer1, TikSerializer, CandidateInfoSerializer, \
    ProtocolFirstSerializer, ProtocolSecondSerializer, UIKSerializer


def get_permissions(user_id):
    """get user permission and role"""
    # pylint: disable=no-member
    # """Поулчить роль и доступы пользователя по id"""
    try:
        perms = Permission.objects.filter(user=user_id).all().values_list('uik', flat=True)
    except Permission.DoesNotExist:
        msg = f"No permissions" \
              f" for {user_id} on uik"
        raise exceptions.PermissionDenied(msg) from Permission.DoesNotExist  # pylint: disable=no-member
    try:
        role = Role.objects.filter(user=user_id).first()
    except Permission.DoesNotExist:
        msg = f"No role" \
              f" for user {user_id}"
        raise exceptions.PermissionDenied(msg) from Role.DoesNotExist  # pylint: disable=no-member

    return list(perms), role.role_user


def has_permission_for(user_id, uik, role):
    """Првоерить, есть ли у пользователя доступ к УИК"""
    perms, user_role = get_permissions(user_id)
    return (uik in perms and user_role == role) or user_role == "ЦИК"  # ЦИК


class ProtocolFirst(APIView):
    """Создать и получить протокол"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProtocolFirstSerializer

    def post(self, request):
        # pylint: disable=no-member
        """Создать новый протокол первого типа"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        protocol = serializer.validated_data

        uik = protocol['num_uik']
        queryset = Uik.objects.filter(id=uik.id)
        uik_table = UIKSerializer(queryset, many=True)
        if not has_permission_for(request.user.id, uik.id, 'УИК'):
            raise exceptions.PermissionDenied()

        inner_num = Protocol1.objects.filter(num_uik=uik.id).count() + 1
        if inner_num > 5:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer.validated_data['num_protocol_1'] = inner_num

        serializer.is_valid(raise_exception=True)
        serializer.save()

        Uik.objects.filter(id=uik.id).update(status=protocol['status'])

        if protocol['sum_bul'] != 0:
            # Uik.objects.filter(id=uik.id).update(presence=F("presence") + protocol['sum_bul'])
            Uik.objects.filter(id=uik.id).update(
                presence=(protocol['sum_bul'] / uik_table.data[0]['population']) * 100,
                sum_votes=protocol['sum_bul']
            )
        if protocol['bad_form'] != 0:
            Uik.objects.filter(id=uik.id).update(bad_form=F("bad_form") + protocol['bad_form'])

        if inner_num == 5:
            Uik.objects.filter(id=uik.id).update(
                sum_numb_votes_fin=protocol['sum_final_bul']
            )

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def get(request, prot_id):
        # pylint: disable=no-member
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
        # pylint: disable=no-member
        """Все протоколы с данного участка"""
        perm, role = get_permissions(request.user.id)
        if uik_id not in perm and role != "ЦИК":
            raise exceptions.PermissionDenied()

        protocols = Protocol1.objects.filter(num_uik=uik_id). \
                        order_by('id')[(page - 1) * 10:page * 10]
        serializer_class = ProtocolFirstSerializer(protocols, many=True)

        data = serializer_class.data
        if len(data) == 5:
            queryset = Protocol2.objects.all().filter(num_uik=uik_id).order_by('name')
            protocol_second_serializer_class = ProtocolSecondSerializer(queryset, many=True)
            data[4]['candidates'] = protocol_second_serializer_class.data

        return Response(data, status=status.HTTP_200_OK)


class ProtocolsFirstListQuantity(APIView):
    """Количество протоколов на участке для пагинации"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, uik_id):
        # pylint: disable=no-member
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

    @staticmethod
    def get(request, page):
        # pylint: disable=no-member
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

    @staticmethod
    def get(request):
        # pylint: disable=no-member
        """Получить количество доступных УИК"""
        perm, role = get_permissions(request.user.id)
        quantity = len(perm)
        if role == "ЦИК":
            quantity = Uik.objects.count()

        return Response({
            'quantity': quantity,
        }, status=status.HTTP_200_OK)


class TikAvailableList(APIView):
    """tik api"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, page):
        # pylint: disable=no-member
        """get list of tiks"""
        _, role = get_permissions(request.user.id)
        if role != "ЦИК":
            raise exceptions.PermissionDenied()

        queryset = Tik.objects.order_by('id').values('num_tik'). \
                       distinct()[(page - 1) * 10:page * 10]

        return Response(list(queryset), status=status.HTTP_200_OK)


class TikAvailableQuantity(APIView):
    """uik api"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        # pylint: disable=no-member
        """get quantity of tiks"""
        _, role = get_permissions(request.user.id)
        if role != "ЦИК":
            raise exceptions.PermissionDenied()

        queryset = Tik.objects.values('num_tik').distinct().count()

        return Response({
            'quantity': queryset
        }, status=status.HTTP_200_OK)


class TikInfo(APIView):
    """tik api"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, name):
        # pylint: disable=no-member
        """get quantity of tiks"""
        _, role = get_permissions(request.user.id)
        if role != "ЦИК":
            raise exceptions.PermissionDenied()

        queryset = Tik.objects.filter(num_tik=name)
        serializer_class = TikSerializer(queryset, many=True)

        return Response(serializer_class.data, status=status.HTTP_200_OK)


class TikCandidates(APIView):
    """tik candidates api"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, name):
        # pylint: disable=no-member
        """get candidates from tiks"""
        _, role = get_permissions(request.user.id)
        if role != "ЦИК":
            raise exceptions.PermissionDenied()

        queryset = Candidate.objects.raw("""
        select c.id, c.name, c.party, c.info, sum(p.candidate_votes) as sum_votes, c.photo
            from mainapp_protocol2 as p
            inner join mainapp_candidate as c on p.name_id=c.id
            inner join mainapp_uik as u on p.num_uik_id=u.id
            where u.num_tik=%s
            group by c.id
        """, params=[name])
        serializer_class = CandidateInfoSerializer(queryset, many=True)

        return Response(serializer_class.data, status=status.HTTP_200_OK)


class ProtocolSecondCreate(APIView):
    """protocol api"""
    permission_classes = [IsAuthenticated]
    serializer_class = ProtocolSecondSerializer

    def post(self, request):
        # pylint: disable=no-member
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


class CandidateViewSet(APIView):
    """
    вся информация по кандидатам в порядке следования в бюллетенях
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable=no-member
        """
        вся информация по кандидатам в порядке следования в бюллетенях
        """
        sum_votes = Uik.objects.aggregate(Sum('sum_votes'))
        sum_votes_sum = sum_votes['sum_votes__sum']
        queryset = Candidate.objects.all().order_by('id')
        serializer_class = VotesSerializer(queryset, many=True)

        for element in serializer_class.data:
            element['sum_votes'] = f"{round((element['sum_votes'] / sum_votes_sum) * 100, 1)}%"

        return response.Response(serializer_class.data)


class CandidateDescVotesViewSet(APIView):
    """
    вся информация по кандидатам в порядке убывания голосов
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        """
        вся информация по кандидатам в порядке убывания голосов
        """
        # pylint: disable=no-member
        sum_votes = Uik.objects.aggregate(Sum('sum_votes'))
        sum_votes_sum = sum_votes['sum_votes__sum']
        queryset = Candidate.objects.all()
        serializer_class = VotesSerializer(queryset, many=True)
        for element in serializer_class.data:
            element['sum_votes'] = round((element['sum_votes'] / sum_votes_sum) * 100, 1)
            birthday = element['birthday'].split('-')
            birthday[0], birthday[2] = birthday[2], birthday[0]
            element['birthday'] = '.'.join(birthday)

        result_list = sorted(serializer_class.data, key=lambda k: k['sum_votes'], reverse=True)

        return response.Response(result_list)


class AccountPermissionsViewSet(viewsets.ModelViewSet):  # pylint: disable = too-many-ancestors
    """Уики доступные аккаунту"""
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def list_of_role_uik(request):
        # pylint: disable = no-member
        """Уики доступные аккаунту"""
        user = request.user
        user_role = Role.objects.get(user_id=user.id)
        role = RoleSerializer(user_role)
        new_dict = {}
        new_dict.update(role.data)
        if user_role.role_user == 'ЦИК':
            return response.Response(new_dict)
        user_uik = Permission.objects.get(user_id=user.id)
        num_uik = Uik.objects.get(pk=user_uik.uik_id)
        uik = UikSerializer(num_uik)
        new_dict.update(uik.data)
        return response.Response(new_dict)


class PresenceViewSet(APIView):
    """
    информация о явке в процентах
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable = no-member
        """
        информация о явке в процентах
        """
        queryset = Tik.objects.values('update_time').annotate(presence=Count('id'))[:1]
        if len(queryset) == 0:
            return response.Response("[]")

        number_tik = queryset[0]['presence']
        queryset = Tik.objects.all().order_by('-update_time', '-presence')[:number_tik]  #
        serializer_class = PresenceSerializer(queryset, many=True)
        return response.Response(serializer_class.data)


class Top24PresenceViewSet(APIView):  # переднлаь под другую таблицу
    """
    топ2-4 УИКов по явке
    'top_presence' список тиков с явкой
    'min_presence' на табло - На этих участках знаение явки привысело 'min_presence' процентов
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable = no-member
        """
        топ2-4 УИКов по явке
        'top_presence' список тиков с явкой
        'min_presence' на табло - На этих участках знаение явки привысело 'min_presence' процентов
        """
        queryset = Tik.objects.all().order_by('-update_time', '-presence')[1:4]
        serializer_class = PresenceSerializer(queryset, many=True)
        new_list = serializer_class.data
        if len(new_list) == 0:
            return response.Response("[]")

        new_list.append({'min_presence': new_list[-1]['presence']})

        return response.Response(new_list)


class TopPresenceViewSet(APIView):
    """
    топ ТИКов по явке
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable = no-member
        """
        топ ТИКов по явке
        """
        queryset = Tik.objects.all().order_by('-presence')[:1]
        serializer = PresenceSerializer(queryset, many=True)

        if len(serializer.data) == 0:
            return response.Response("{}")
        return response.Response(serializer.data[0])


class TopTikViewSet(APIView):
    """Информация о топе тиков по времени"""
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable = no-member
        """Информация о топе тиков по времени"""
        queryset = Tik.objects.all().order_by('-population')[:1]
        serializer = TopTikSerializer1(queryset, many=True)
        if len(serializer.data) == 0:
            return response.Response("{}")

        return response.Response(serializer.data[0])


class GeneralInfoViewSet(APIView):
    """
    количество открытых участков и избирателей
    """
    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable = no-member
        """
        количество открытых участков и избирателей
        """
        result_dict = {}
        result_dict.update(Uik.objects.aggregate(population=Sum('population')))
        result_dict.update(Uik.objects.filter(status=True).aggregate(open_uik=Count('id')))
        return response.Response(result_dict)


class GeneralInfoPresenceViewSet(APIView):
    """
    количество открытых участков,охваченных избирателей и явка
    """

    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable = no-member
        """
        количество открытых участков,охваченных избирателей и явка
        """
        result_dict = {}
        result_dict.update(Uik.objects.filter(status=True). \
                           aggregate(open=Count('id')))
        result_dict.update(Uik.objects.filter(status=True). \
                           aggregate(sum_electorators=Sum('population')))
        presence = Uik.objects.filter(status=True). \
            aggregate(sum_vot=Sum('sum_votes'),
                      sum_pop=Sum('population'))
        presence = f"{round((presence['sum_vot'] / presence['sum_pop']) * 100, 1)}%"
        result_dict.update({'presence': presence})

        return response.Response(result_dict)


class VotesPresenceViewSet(APIView):
    """
    явка и процент обработанных бюллетеней
    """

    permission_classes = [
        permissions.IsAuthenticated
    ]

    @staticmethod
    def get(_):
        # pylint: disable = no-member
        """
        явка и процент обработанных бюллетеней
        """
        result_dict = {}
        percent = Uik.objects. \
            aggregate(sum_votes_fin=Sum('sum_numb_votes_fin'),
                      sum_votes=Sum('sum_votes'))
        result_dict. \
            update({'percent_votes':
                        f"{round((percent['sum_votes_fin'] / percent['sum_votes']) * 100)}%"})

        presence = Uik.objects.filter(status=True). \
            aggregate(population=Sum('population'), sum_votes=Sum('sum_votes'))
        result_dict.update({'presence':
                            f"{round((presence['sum_votes'] / presence['population']) * 100)}%"})

        return response.Response(result_dict)
