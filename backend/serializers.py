from rest_framework import serializers

from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'identifier'
        )


class IssusingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emisor
        fields = (
            'id',
            'name',
            'identifier'
        )


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            'token',
            'status'
        )


class UserProfileSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'app_installed',
            'first_name',
            'last_name',
            'email',
            'account',
        )
