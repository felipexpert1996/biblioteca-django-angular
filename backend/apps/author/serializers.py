from rest_framework.serializers import ModelSerializer

from apps.author.models import Author
from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class AuthorSerializer(ModelSerializer):

    category = CategorySerializer(many=True, read_only=False)

    class Meta:
        model = Author
        fields = ['name', 'category']

    def create(self, validated_data):
        category = validated_data['category']
        del validated_data['category']
        author = Author.objects.create(**validated_data)
        self.crete_categories(category, author)
        return author

    def update(self, instance, validated_data):
        author = Author.objects.get(pk=instance.pk)
        author.name = validated_data['name']
        author.save()
        category = validated_data['category']
        del validated_data['category']
        self.crete_categories(category, author)
        return author

    @staticmethod
    def crete_categories(categories, author):
        author.category.clear()
        for category in categories:
            category = Category.objects.create(**category)
            author.category.add(category)
