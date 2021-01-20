from django.contrib.auth.models import User
from django.test import TestCase
from faker.providers import internet, misc
from rest_framework.test import APITestCase, APIClient, force_authenticate
from faker import Faker
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from apps.category.models import Category


class CategoryTest(APITestCase):
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

    def test_create(self):
        url = reverse('category-list')
        fake = Faker()
        fake.add_provider(misc)
        data = {'description': fake.user_name()}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.filter(description=data['description']).exists(), True)

    def test_list(self):
        url = reverse('category-list')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        category = self.get_category()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[-1], {'description': category.description})

    def test_update(self):
        category = self.get_category()
        url = reverse('category-detail', kwargs={'pk': category.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        fake = Faker()
        fake.add_provider(misc)
        data = {'description': fake.user_name()}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], data['description'])

    def test_delete(self):
        category = self.get_category()
        url = reverse('category-detail', kwargs={'pk': category.pk})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.get_token())
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.filter(description=category.description).exists(), False)

