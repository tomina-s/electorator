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

    def view_candidate_info(self, request):
        """TODO: запрос на получение инфы по конкретному кандидату по id.

        :param request:
        :return:
        """
        queryset = Candidate.objects.all()
        # candidate_id = request

        # надо разобраться что такое permission_classes
        # permission_classes = [
        #     permissions.AllowAny
        # ]
        serializer_class = CandidatInfoSerializer(queryset, many=True)
        return response.Response(serializer_class.data)


class ProtocolViewSet(viewsets.ModelViewSet):
    """Протокол.

    GET /protocol - получить все протоколы, к которым пользователь имеет доступ
    GET /protocol/{id} - получить информацию о протоколе по его id.  Нужно проверять,
    есть ли у пользователя на это права!

    """

    def list(self, request):
        """GET /protocol - получить все протоколы, к которым пользователь имеет доступ."""

        permission_classes = [
            permissions.AllowAny
        ]
        current_id_user = request.user.id
        user_role = Role.objects.get(user_id=current_id_user)
        # RoleSerializer

        queryset = Protocol1.objects.all()
        serializer_class = Protocol1Serializer(queryset, many=True)

        **.objects.filter(purchaser=user)

        Protocol1.objects.filter(contractor=request.user.id)
        # Protocol2.objects.filter(contractor=request.user.id)

        return response.Response(serializer_class.data)





#  examples
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------

from .models import Candidate
from rest_framework import viewsets, permissions, response
from .serializers import CandidateSerializer, CandidatInfoSerializer
from rest_framework.decorators import action

# мб еще импорты по сералайзеру должны быть и другие классы из сериалайзера


class CandidateViewSet(viewsets.ModelViewSet):

    """
    ViewSet для отображения данных по кандидатам.

    Кандидат - чтение (модели).
    list_of_candidats - чтение всех кандидатов на данных выборах.

    user_list = CandidateViewSet.as_view({'get': 'list_of_candidats'})
    user_detail = CandidateViewSet.as_view({'get': '***'})

    """

    def list_of_candidats(self, request):
        queryset = Candidate.objects.all()
        permission_classes = [
            permissions.AllowAny
        ]
        #  что за переменная класса CandidateSerializer?
        # здесь в апи или в сериалайзере прописывать какие поля Модели нужны для этого метода -
        # наверно в сериалайзере
        #     например: для list_of_candidats нужно только поле "name"

        # нужно ли использовать атрибут ф-ции request?
        serializer_class = CandidateSerializer(queryset, many=True)
        return response.Response(serializer_class.data)


    def view_candidate_info(self, request):
        queryset = Candidate.objects.all()
        # надо разобраться что такое permission_classes
        # permission_classes = [
        #     permissions.AllowAny
        # ]
        serializer_class = CandidatInfoSerializer(queryset, many=True)

        #
        # Article - model
        queryset= Article.objects.all().filter(category=14).order_by('-created')[:10]

        return response.Response(serializer_class.data)


#  examples
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
