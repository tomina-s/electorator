from rest_framework import serializers
# from .models import DB_test
from .models import Candidate, Protocol1, Protocol2


class DB_testSerializer(serializers.ModelSerializer):
    class Meta:
        pass


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name"]


# TODO: пока не используется - мб убрать
class CandidatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name", "info", "sum_votes"]


class Protocol1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol1
        fields = '__all__'


class Protocol2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol2
        fields = '__all__'

# пока не нужно
# class UikProtocol1Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Protocol1
#         fields = ['id_protocol1']


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


