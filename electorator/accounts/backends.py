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

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = self.authentication_header_prefix.lower()

        if not auth_header:
            return None

        if len(auth_header) == 1:
            return None
        elif len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return None

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            msg = 'Unable to decode jwt'
            raise exceptions.AuthenticationFailed(msg)

        try:
            user = Account.objects.get(pk=payload['id'])
        except Account.DoesNotExist:
            msg = 'User with id=%d doesnt exist' % payload['id']
            raise exceptions.AuthenticationFailed(msg)

        return user, token