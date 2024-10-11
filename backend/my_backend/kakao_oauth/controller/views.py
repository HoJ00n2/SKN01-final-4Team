import uuid

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from account.service.account_service_impl import AccountServiceImpl
from kakao_oauth.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from kakao_oauth.serializer.kakao_oauth_url_serializer import KakaoOauthUrlSerializer
from kakao_oauth.service.kakao_oauth_service_impl import KakaoOauthServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl

class KakaoOauthView(viewsets.ViewSet):
    kakao_oauthService = KakaoOauthServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()

    def kakaoOauthURI(self, request):
        url = self.kakao_oauthService.kakaoLoginAddress()
        print(f"url:", url)
        serializer = KakaoOauthUrlSerializer(data={ 'url': url })
        serializer.is_valid(raise_exception=True)
        print(f"validated_data: {serializer.validated_data}")
        return Response(serializer.validated_data)

    def kakaoAccessTokenURI(self, request):
        serializer = KakaoOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            accessToken = self.kakao_oauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return JsonResponse({'accessToken': accessToken})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def kakaoUserInfoURI(self, request):
        accessToken = request.data.get('access_token')
        print(f'accessToken: {accessToken}')

        try:
            user_info = self.kakao_oauthService.requestUserInfo(accessToken)
            return JsonResponse({'user_info': user_info})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

