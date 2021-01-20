from rest_framework.serializers import ModelSerializer

from apps.category.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['description']
