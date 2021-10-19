from .models import Candidate
from rest_framework import viewsets, permissions, response
from .serializers import CandidateSerializer, CandidatInfoSerializer

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
        return response.Response(serializer_class.data)


#  examples
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
