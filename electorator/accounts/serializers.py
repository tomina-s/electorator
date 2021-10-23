from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Role, Permission

from .models import Account


class LoginSerializer(serializers.Serializer):
    snils = serializers.CharField(max_length=11, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        snils = data.get('snils', None)
        password = data.get('password', None)

        if snils is None or len(snils) != 11:
            raise serializers.ValidationError(
                'snils is required and must be valid to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'password is required to log in.'
            )

        account = authenticate(username=snils, password=password)

        if account is None:
            raise serializers.ValidationError(
                'A user with this snils and password was not found.'
            )

        return account


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['user', 'role']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['user', 'uik']
