from .models import Candidate, Protocol1, Protocol2
from ..accounts.models import Role, Permission
from rest_framework import viewsets, permissions, response
from .serializers import CandidateSerializer, CandidatInfoSerializer, Protocol1Serializer, Protocol2Serializer


'''
GET /protocol - получить все протоколы, к которым пользователь имеет доступ
GET /protocol/{id} - получить информацию о протоколе по его id.  Нужно проверять,
есть ли у пользователя на это права!

GET /account/permissions  - получить роль пользувателя и доступные уики
GET /candidate - получить список кандидатов
'''


class CandidateViewSet(viewsets.ModelViewSet):

    """
    ViewSet для отображения данных по кандидатам.

    Кандидат - чтение (модели).
    list_of_candidats - чтение всех кандидатов на данных выборах.

    user_list = CandidateViewSet.as_view({'get': 'list_of_candidats'})
    user_detail = CandidateViewSet.as_view({'get': '***'})

    """

    def list(self, request):
        """GET /candidate - получить список кандидатов."""

        queryset = Candidate.objects.all()
        permission_classes = [
            permissions.AllowAny
        ]
        serializer_class = CandidateSerializer(queryset, many=True)
        return response.Response(serializer_class.data)


'''
пример
www.django-rest-framework.org/api-guide/filtering

url('^purchases/(?P.+)/$', PurchaseList.as_view()),

class PurchaseList(generics.ListAPIView):
serializer_class = PurchaseSerializer

def get_queryset(self):
    """
    This view should return a list of all the purchases for
    the user as determined by the username portion of the URL.
    """
    username = self.kwargs['username']
    return Purchase.objects.filter(purchaser__username=username)
'''


class ProtocolViewSet(viewsets.ModelViewSet):
    """Протокол.

    GET /protocol - получить все протоколы, к которым пользователь имеет доступ
    GET /protocol/{id} - получить информацию о протоколе по его id.  Нужно проверять,
    есть ли у пользователя на это права!

    """

    def list(self, request):
        """GET /protocol - получить все протоколы, к которым пользователь имеет доступ.

        :return два массива с протоколами 1 и второго типа по отдельности.
        """

        permission_classes = [
            permissions.IsAuthenticated
        ]
        # получение юзера и user.id
        user = request.user
        # получение роли юзера
        user_role = Role.objects.get(user_id=user.id)

        # получили уик
        uik = Permission.objects.filter(purchaser=user)
        # получение протоколов по этому уику
        queryset_prot1 = Protocol1.onjects.filter(purchase=uik)
        queryset_prot2 = Protocol2.onjects.filter(purchase=uik)

        serializer_class1 = Protocol1Serializer(queryset_prot1, meny=True)
        serializer_class2 = Protocol2Serializer(queryset_prot2, meny=True)

        # example:  Article - model
        # queryset= Article.objects.all().filter(category=14).order_by('-created')[:10]
        # serializer_class = Protocol1Serializer(queryset, many=True)

        # Protocol1.objects.filter(contractor=request.user.id)
        # Protocol2.objects.filter(contractor=request.user.id)
        return response.Response(serializer_class1.data), response.Response(serializer_class2.data)