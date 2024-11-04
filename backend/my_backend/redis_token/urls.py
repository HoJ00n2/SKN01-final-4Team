from django.urls import path, include
from rest_framework.routers import DefaultRouter
from redis_token.controller.views import RedisTokenView

router = DefaultRouter()
router.register(r'redis_token', RedisTokenView, basename='redis_token')

urlpatterns = [
    path('', include(router.urls)),
    path('redis-access-token', RedisTokenView.as_view({'post': 'redisAccessToken'}), name='redis-access-token'),
    path('logout', RedisTokenView.as_view({'post': 'dropRedisTokenForLogout'}), name='drop-redis-token-for-logout')
]