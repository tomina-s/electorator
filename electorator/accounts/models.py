"""
accounts model and model manager
"""
from datetime import (
    datetime, timedelta
)
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
import jwt

from mainapp.models import Uik


class AccountManager(BaseUserManager):
    """Model manager forbids to create user via django-admin"""
    @staticmethod
    def create_user(email, password=None):
        """Model manager forbids to create user via django-admin"""
        raise RuntimeError('Users must be created via CLI')

    @staticmethod
    def create_superuser(email, password):
        """Model manager forbids to create user via django-admin"""
        raise RuntimeError('Users must be created via CLI')


class Account(AbstractBaseUser):
    """Account model is used to replace default authorization"""
    objects = AccountManager()
    name = models.CharField(
        verbose_name='ФИО',
        max_length=300,
        unique=False,
    )
    username = models.CharField(
        verbose_name='Номер СНИЛС',
        max_length=30,
        unique=True,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """account is defined by username"""
        return self.username

    def get_short_name(self):
        """account is defined by username"""
        return self.username

    def __str__(self):
        """account is defined by username"""
        return str(f'{self.username}')

    def get_jwt_token(self):
        """generates jwt out of account id"""
        date_time = datetime.now() + timedelta(days=60)

        token = jwt.encode(payload={
            'id': self.pk,
            'exp': int(date_time.strftime('%s'))
        }, key=settings.SECRET_KEY, algorithm='HS256')

        return token




class Permission(models.Model):
    """Permission table"""
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    uik = models.OneToOneField(Uik, on_delete=models.CASCADE)


class Role(models.Model):
    """Role table"""
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    role_user = models.CharField(max_length=20)

