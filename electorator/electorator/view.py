from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class MockView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        response = Response("hello", status=status.HTTP_200_OK)

        return response
