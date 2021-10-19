from rest_framework import serializers
# from .models import DB_test
from .models import Candidate


class DB_testSerializer(serializers.ModelSerializer):
    class Meta:
        pass


# Кандидат - чтение (модели), чтение всех кандидатов на данных выборах.

# может быть несоклько сериализаторов для одной модеели

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name"]


class CandidatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["name", "info", "sum_votes"]


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


