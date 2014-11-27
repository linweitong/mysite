from rest_framework import authentication
from models import VSUser
from rest_framework import exceptions, HTTP_HEADER_ENCODING


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

    def get_authorization_header2(self, request):
        """
        Return request's 'VSAuthorization:' header, as a bytestring.

        Hide some test client ickyness where the header can be unicode.
        """
        auth = request.META.get('HTTP_VSACCESSTOKEN', b'')
        if isinstance(auth, type('')):
            # Work around django test client oddness
            auth = auth.encode(HTTP_HEADER_ENCODING)
        return auth

    def authenticate(self, request):
        auth = self.get_authorization_header2(request).split()

        if not auth:
            return None

        if len(auth) > 1:
            msg = 'Invalid token header. Token string should not contain spaces.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(auth[0])