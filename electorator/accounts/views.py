"""This view provides handlers for logging only"""
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
        """login handler"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        account = serializer.validated_data
        perm = Permission.objects.filter(user=account.id).all()
        uik_id = 'uik_id'
        permissions = []
        for v in perm:
            permissions.append(getattr(v, uik_id))

        role = Role.objects.filter(user=account.id).first()
        role_user = 'role_user'

        response = Response(
            {
                'jwt': account.get_jwt_token(),
                'role': getattr(role, role_user),
                'permissions': permissions,
            },
            status=status.HTTP_200_OK
        )
        return response


class Permissions(APIView):
    """read user permissions"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """read user permissions"""
        user_id = request.user.id
        perm = Permission.objects.filter(user=user_id).all()
        uik_id = 'uik_id'
        permissions = []
        for v in perm:
            permissions.append(getattr(v, uik_id))

        return Response({
            'permissions': permissions,
        }, status=status.HTTP_200_OK)


class Roles(APIView):
    """read user role"""
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        """read user role"""
        user_id = request.user.id
        role = Role.objects.filter(user=user_id).first()
        role_user = 'role_user'

        return Response({
            'role': getattr(role, role_user),
        }, status=status.HTTP_200_OK)
