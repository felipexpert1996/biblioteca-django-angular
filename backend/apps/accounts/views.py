from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LogoutView, LoginView
from rest_framework.generics import RetrieveAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomRegisterView(RegisterView):
    """
    Register a new user, return an access token.

    Accept the following POST parameters: username, email, password1, password2
    Return the REST Framework Token Object's key.
    """

    
class CustomLogoutView(LogoutView):
    """
    Calls Django logout method and delete the Token object
    assigned to the current User object.
    
    Token must be sent in the request header.

    Accepts/Returns nothing.
    """

    http_method_names = ["post"]


class CustomLoginView(LoginView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.

    Calls Django Auth login method to register User ID
    in Django session framework.

    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """

class VerifyToken(RetrieveAPIView):
    """
    Checks if the token is valid and returns a boolean.

    Checks the existence of the token in the database.

    Receives a query string with user email
    """

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        email = request.query_params.get("email")
        if (token and email):
            return Response({'valid':Token.objects.filter(key=token, user__email=email).exists()})
        else:
            return Response({'valid':False})