from rest_framework import serializers

from account.entity.account import Account
from account.entity.profile import Profile


class AccountSerializer(serializers.ModelSerializer):
    loginType = serializers.CharField(source='loginType.loginType', read_only=True)
    roleType = serializers.CharField(source='roleType.roleType', read_only=True)

    class Meta:
        model = Account
        fields = ['id', 'loginType', 'roleType']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email', 'nickname']
