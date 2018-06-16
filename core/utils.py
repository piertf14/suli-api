from oauth2_provider.models import AccessToken


def get_access_token(request):
    authorization_header = request.META.get('HTTP_AUTHORIZATION')
    type_authorization, token = authorization_header.split()
    access_token = AccessToken.objects.get(token=token)
    return access_token