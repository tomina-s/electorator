from django.conf import settings
import jwt
from rest_framework import (
    authentication, exceptions
)

from .models import Account


class JWTAuthentication(authentication.BaseAuthentication):
    authentication_header_prefix = 'Token'

    def authenticate(self, request):
        request.user = None

        token = request.COOKIES.get('jwt')
        if token is None:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256', ])
        except Exception:
            msg = 'Unable to decode jwt'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = Account.objects.get(pk=payload['id'])
        except Account.DoesNotExist:
            msg = 'User with id=%d doesnt exist' % payload['id']
            raise exceptions.AuthenticationFailed(msg)

        return user, token
