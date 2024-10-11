from django.urls import path, include
from rest_framework.routers import DefaultRouter
from naver_oauth.controller.views import NaverOauthView

router = DefaultRouter()
router.register(r'naver_oauth', NaverOauthView, basename='naver_oauth')
urlpatterns = [
    path('', include(router.urls)),
    path('naver', NaverOauthView.as_view({'get': 'naverOauthURI'}), name='get-naver-oauth-uri'),
    path('naver/access-token', NaverOauthView.as_view({'post': 'naverAccessTokenURI'}), name='get-naver-access-token'),
    path('naver/user-info', NaverOauthView.as_view({'post': 'naverUserInfoURI'}), name='get-naver-user-info-uri'),
]
