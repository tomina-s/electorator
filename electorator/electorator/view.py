from rest_framework import status

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Account
#from accounts.models import Permit
#from accounts.models import Role


from django.db import models


class MockView(APIView):
    permission_classes = [AllowAny] #AllowAny IsAuthenticated

    def perm(self,request):
        user = request.user
        user_id = user.id
        user_id_DB = Account.objects.get(pk=user_id)
        print('Iamhere')
        if not user_id_DB:
            response = Response(status=status.HTTP_403_FORBIDDEN)
        else:
            response = Response(status=status.HTTP_200_OK)
        return response


        #user.id  == user из базы ?
        # если да, то работаем лдальше
        # если нет, response(403) #todo


    def get(self, request):
        return Response('hello')
        #user = request.user
        #user_id_DB = Account.objects.get(pk=user.id)
        #if not user_id_DB:
        #    response = Response(status=status.HTTP_403_FORBIDDEN)
        #else:
        #    response = Response(status=status.HTTP_200_OK)
        #return response




    #curl - H
    #"Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MiwiZXhwIjoxNjM5OTI2ODAyfQ.aIj-9vZaWEj0FE-7XysHs6UYysINrjtNE9YBo6hfkW8"
    #http: // localhost: 8000 / api / mockview /