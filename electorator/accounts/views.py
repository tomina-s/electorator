"""This view provides handlers for logging only"""
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer


class LoginAPIView(APIView):
    """login api"""
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """login handler"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = serializer.validated_data

        response = Response(
            {'jwt': account.get_jwt_token()},
            status=status.HTTP_200_OK
        )

        return response
