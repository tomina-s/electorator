from datetime import (
    datetime, timedelta
)
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
import jwt


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None):
        raise RuntimeError('Users must be created via CLI')

    def create_superuser(self, email, password):
        raise RuntimeError('Users must be created via CLI')


class Account(AbstractBaseUser):
    objects = AccountManager()
    name = models.CharField(
        verbose_name='ФИО',
        max_length=300,
        unique=False,
    )
    snils = models.CharField(
        verbose_name='Номер СНИЛС',
        max_length=11,
        unique=True,
    )

    USERNAME_FIELD = 'snils'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.snils

    def get_short_name(self):
        return self.snils

    def __str__(self):
        return self.snils

    def get_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
