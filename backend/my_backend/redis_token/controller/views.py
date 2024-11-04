import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response
from account.service.account_service_impl import AccountServiceImpl
from redis_token.service.redis_service_impl import RedisServiceImpl


class RedisTokenView(viewsets.ViewSet):
    accountService = AccountServiceImpl.getInstance()
    redisService = RedisServiceImpl.getInstance()

    def redisAccessToken(self, request):
        try:
            email = request.data.get('email')
            print(f"redisAccessToken -> email: {email}")

            account = self.accountService.findAccountByEmail(email)
            if not account:
               return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            # 랜덤한 값을 만들어 userToken으로 준다.
            # random함수를 사용하는 것 보다 중복 가능성이 낮아 uuid4를 사용
            userToken = str(uuid.uuid4())
            self.redisService.storeAccessToken(account.id, userToken)

            accountId = self.redisService.getValueByKey(userToken)
            print(f"after redis_token' convert accountId: {accountId}")

            return Response({'userToken': userToken}, status=status.HTTP_200_OK)
        except Exception as e:
            print('Error storing access token in Redis:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def dropRedisTokenForLogout(self, request):
        try:
            userToken = request.data.get('userToken')
            isSuccess = self.redisService.deleteKey(userToken)
            return Response({'isSuccess': isSuccess}, status=status.HTTP_200_OK)
        except Exception as e:
            print('레디스 토큰 해제 중 에러 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)