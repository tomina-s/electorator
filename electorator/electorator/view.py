from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class MockView(APIView):
    permission_classes = [IsAuthenticated]

    def perm(self,request):
        #user.id  == user из базы ?
        # если да, то работаем лдальше
        # если нет, response( 403) #todo
        pass


    def get(self, request):
        response = Response("hello", status=status.HTTP_200_OK)

        return response

