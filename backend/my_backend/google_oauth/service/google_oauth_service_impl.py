from my_backend import settings
from google_oauth.service.google_oauth_service import GoogleOauthService
import requests
import urllib.parse

class GoogleOauthServiceImpl(GoogleOauthService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.loginUrl = settings.GOOGLE['LOGIN_URL']
            cls.__instance.clientId = settings.GOOGLE['CLIENT_ID']
            cls.__instance.redirectUri = settings.GOOGLE['REDIRECT_URI']
            cls.__instance.clientSecret = settings.GOOGLE['CLIENT_SECRET']
            cls.__instance.tokenRequestUri = settings.GOOGLE['TOKEN_REQUEST_URI']
            cls.__instance.userinfoRequestUri = settings.GOOGLE['USERINFO_REQUEST_URI']
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def googleLoginAddress(self):
        print("googleLoginAddress()")
        scopes = "profile email"  # 여러 스코프를 공백으로 구분
        encoded_scopes = urllib.parse.quote(scopes)  # URL 인코딩
        return (f"{self.loginUrl}/oauth2/v2/auth?"
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}"
                f"&response_type=code&scope={encoded_scopes}")

    def requestAccessToken(self, googleAuthCode):
        accessTokenRequestForm = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            'code': googleAuthCode,
            'client_secret': self.clientSecret
        }
        response = requests.post(self.tokenRequestUri, data=accessTokenRequestForm)
        return response.json()

    def requestUserInfo(self, accessToken):
        headers = {'Authorization': f'Bearer {accessToken}'}
        response = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', headers=headers)
        # response = requests.post(self.userinfoRequestUri, headers=headers)
        return response.json()
