"""This view provides handlers for logging only"""
from django.core import exceptions
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Permission, Role
from .serializers import LoginSerializer


class Login(APIView):
    """login api"""
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        # pylint: disable=no-member
        """login handler"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = serializer.validated_data
        perm = Permission.objects.filter(user=account.id).all().values_list('uik', flat=True)

        role = Role.objects.filter(user=account.id).first()
        if not role:
            raise exceptions.PermissionDenied()

        response = Response(
            {
                'jwt': account.get_jwt_token(),
                'role': role.role_user,
                'permissions': perm,
            },
            status=status.HTTP_200_OK
        )
        return response


class Permissions(APIView):
    """read user permissions"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        # pylint: disable=no-member
        """read user permissions"""
        user_id = request.user.id
        permissions = Permission.objects.filter(user=user_id).all().values_list('uik', flat=True)

        return Response({
            'permissions': permissions,
        }, status=status.HTTP_200_OK)


class Roles(APIView):
    """read user role"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        # pylint: disable=no-member
        """read user role"""
        user_id = request.user.id
        role = Role.objects.filter(user=user_id).first()

        return Response({
            'role': role.role_user,
        }, status=status.HTTP_200_OK)
