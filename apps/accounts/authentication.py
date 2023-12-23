from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.request import Request

from .models import ShmisUser


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: Request):
        api_key = request.query_params.get('api_key')

        if not api_key:
            return None

        try:
            user = ShmisUser.objects.get(api_key=api_key, banned=False, activation_code=None)
            print(user)
        except ShmisUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid API Key or banned/not activated user.')
        return user, None