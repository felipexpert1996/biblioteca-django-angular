from rest_framework.viewsets import ModelViewSet

from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class CategoryViewset(ModelViewSet):
    """
        Provides an api for book categories crud

        Args:
            None

        Returns:
            [
                {
                    "description": "exemplo"
                }
            ]
    """

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
