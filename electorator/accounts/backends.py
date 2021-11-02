"""This module defines custom JWT authorization"""
from django.conf import settings
import jwt
from rest_framework import (
    authentication, exceptions
)

from .models import Account


class JWTAuthentication(authentication.BaseAuthentication):
    """
    JWTAuthentication is inherited from base django class
    Doesnt need csrf token to be used in post, put and delete requests
    """
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        """validates authorization header"""
        request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None
        if len(auth_header) == 1:
            return None
        if len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    @staticmethod
    def _authenticate_credentials(_, token):
        """validates jwt token"""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256', ])
        except Exception as invalid_jwt:
            msg = 'Unable to decode jwt'
            raise exceptions.AuthenticationFailed(msg) from invalid_jwt

        try:
            user = Account.objects.get(pk=payload['id'])
        except Account.DoesNotExist:  # pylint: disable=no-member
            msg = f"User with id={payload['id']} doesnt exist"
            raise exceptions.AuthenticationFailed(msg) from Account.DoesNotExist  # pylint: disable=no-member

        return user, token
