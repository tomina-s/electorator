"""Serializers for accounts"""
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Serializes login and password of user"""
    snils = serializers.CharField(max_length=11, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        snils = attrs.get('snils', None)
        password = attrs.get('password', None)

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

    def create(self, validated_data):
        print("Create not defined")

    def update(self, instance, validated_data):
        print("Update not defined")
