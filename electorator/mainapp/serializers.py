from rest_framework import serializers

from accounts.models import Role
from .models import Candidate, Protocol1, Protocol2, Uik


class ProtocolFirstSerializer(serializers.ModelSerializer):
    """Creation the first protocol"""
    class Meta:
        model = Protocol1
        fields = ['id', 'num_uik', 'num_protocol_1', 'status', 'sum_bul', 'bad_form']


class ProtocolSecondSerializer(serializers.ModelSerializer):
    """Creation of the second protocol"""
    class Meta:
        model = Protocol2
        fields = ['num_uik', 'name', 'candidate_votes']


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "info", "sum_votes"]


class CandidatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name", "info", "sum_votes"]



class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ["role"]


class UikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uik
        fields = ["num_uik"]


'''
# прлписывает ли в БД?
- разобрать рест апи
- чтение кандидата из БД по айди - только чтение
    Сущность - запросы/действия ручек.
Кандидат - чтение (модели), чтение всех кандидатов на данных выборах.
Protocol1 Protocol2  - ручка для создания (возможно что это общая ручка).
            запрос мне приходит - запрос на мой взгляд какой нужен? такой Сережа и сделает.
Uik - чтение всех УИК со всеми полями. с Пагинация - например с 1-10 УИК по id.
    запрос: -! будет гворить диапазон - с какого по какой id
            -  с какого айди передавать инфу - 10 например. выдаю не более 5 например.
опредялал какие пермишионс для авторизированного пользовтеля
- urls.py запонить урлами
'''

