import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from user.models import CustomUser


class CookieJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None  # Let DRF try other authenticators

        try:
            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=['HS256']
            )
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('JWT expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid JWT')

        user_id = payload.get('id')
        if not user_id:
            raise AuthenticationFailed('Invalid payload')

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed('User not found')

        return (user, None)
