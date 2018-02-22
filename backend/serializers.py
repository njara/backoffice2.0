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

    def create(self, validated_data):
        validated_data['id'] = None
        account = Account.objects.create(
            id=validated_data['id'],
            token=validated_data['position'],
            status=validated_data['answer'],
        )
        return account


class UserProfileSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = UserProfile
        fields = (
            'id',
            'username',
            'app_installed',
            'first_name',
            'last_name',
            'email',
            'account',
        )

    def create(self, validated_data):
        account_data = validated_data.pop('account')
        validated_data['id'] = None
        account = Account.objects.create(**account_data)
        validated_data['account'] = account
        userprofile = UserProfile.objects.create(**validated_data)
        return userprofile
