"""Serializers for accounts"""
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Serializes login and password of user"""
    username = serializers.CharField(max_length=30, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username', None)
        password = attrs.get('password', None)

        if username is None or len(username) > 30:
            raise serializers.ValidationError(
                'username is required and must be valid to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'password is required to log in.'
            )

        account = authenticate(username=username, password=password)

        if account is None:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        return account

    def create(self, validated_data):
        print("Create not defined")

    def update(self, instance, validated_data):
        print("Update not defined")
