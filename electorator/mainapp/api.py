from .models import Candidate, Uik
from accounts.models import Account,Permission,Role
from rest_framework import viewsets, permissions, response
from .serializers import CandidateSerializer, CandidatInfoSerializer, RoleSerializer, UikSerializer
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
        c = serializer_class.data
        b=1
        return response.Response(serializer_class.data)

    def view_candidate_info(self, request):
        queryset = Candidate.objects.all()
        # надо разобраться что такое permission_classes
        # permission_classes = [
        #     permissions.AllowAny
        # ]
        serializer_class = CandidatInfoSerializer(queryset, many=True)

        return response.Response(serializer_class.data)


'''GET /account/permissions  - получить роль пользувателя и доступные уики'''


class AccountPermissionsViewSet(viewsets.ModelViewSet):
    def list_of_role_uik(self,request):
        permission_classes = [
            permissions.AllowAny
        ]
        user = request.user# request пустой AnonymousUser (хз почему)
        #заменить ниже user_id на user.id когда рекуест будет не пустой
        user_id = 3
        user_role = Role.objects.get(user_id=user_id)
        role = RoleSerializer(user_role)
        c=1
        if user_role.role == 'ВИК':
            print(type(role.data))
            c=1
            return response.Response(role.data)
        #user_uik = Permission.objects.get(user_id=user.id)
        #num_uik = Uik.objects.get(pk=user_uik.uik_id)
        #uik = UikSerializer(num_uik)

        #return response.Response(uik.data)





        #print(user_role)
        #if Permission.objects.get(pk=user.id):# or Account.objects.get(pk=user.id,role = 'УИК'):
        #    print(Account.objects.get(pk = user.id))


'''
curl -H "Authorization:Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MywiZXhwI
joxNjM5OTI5NTY5fQ.AAhViMxjaiIinQUXwjW2nhApKXtdA6wDBFglpA4AcFY" localhost:8000/api/candidate/permission
'''
