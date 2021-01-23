from collections import OrderedDict

from django.contrib.auth.models import User
from faker.providers import internet, misc, person
from rest_framework.test import APITestCase, APIClient
from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.author.models import Author
from apps.category.models import Category


class AuthorTest(APITestCase):
    client = APIClient()

    @staticmethod
    def get_token():
        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(misc)
        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(misc)
        user = User.objects.create_user(username=fake.user_name(), email=fake.email(), password=fake.password(length=8))
        return Token.objects.create(user=user).key

    @staticmethod
    def get_category():
        fake = Faker()
        fake.add_provider(misc)
        return Category.objects.create(description=fake.user_name())

    def get_author(self):
        fake = Faker()
        fake.add_provider(person)
        author = Author.objects.create(name=fake.name())
        category = self.get_category()
        author.category.add(category)
        return author

    def test_create(self):
        url = reverse('author-list')
        fake = Faker()
        fake.add_provider(person)
        fake.add_provider(misc)
        data = {'name': fake.name(), 'category': [{'description': fake.user_name()}]}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.filter(
            name=data['name'], category__description=data['category'][0]['description']).exists(), True)

    def test_list(self):
        url = reverse('author-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        author = self.get_author()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[-1]['name'], author.name)
        self.assertEqual(
            response.data[-1]['category'][0]['description'],
            Category.objects.get(author__name=response.data[-1]['name']).description)

    def test_update(self):
        author = self.get_author()
        url = reverse('author-detail', kwargs={'pk': author.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        fake = Faker()
        fake.add_provider(person)
        data = {'name': fake.name(), 'category': [{'description': fake.user_name()}]}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['category'][0]['description'], data['category'][0]['description'])

    def test_delete(self):
        author = self.get_author()
        url = reverse('author-detail', kwargs={'pk': author.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.filter(pk=author.pk).exists(), False)
