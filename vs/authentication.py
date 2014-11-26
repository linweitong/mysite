from rest_framework import authentication
from rest_framework import exceptions
from models import VSUser

class TokenAuthentication(authentication.TokenAuthentication):
   def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        token.user = VSUser.objects.get(id=token.user.id)

        return (token.user, token)