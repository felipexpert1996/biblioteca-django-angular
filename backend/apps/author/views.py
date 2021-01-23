from rest_framework.viewsets import ModelViewSet

from apps.author.models import Author
from apps.author.serializers import AuthorSerializer


class AuthorViewset(ModelViewSet):
    """
            Provides an api for book authors crud

            Args:
                None

            Returns:
                [
                   {
                      "name":"",
                      "category":[
                         {
                            "description":""
                         }
                      ]
                   }
                ]
    """

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
