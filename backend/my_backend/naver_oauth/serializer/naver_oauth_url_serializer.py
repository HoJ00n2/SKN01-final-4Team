from rest_framework import serializers
class NaverOauthUrlSerializer(serializers.Serializer):
    url = serializers.URLField()