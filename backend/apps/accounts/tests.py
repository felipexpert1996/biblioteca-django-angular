from rest_framework.test import APITestCase, APIClient
from faker import Faker
from django.urls import reverse
from rest_framework import status
from faker.providers import internet, misc
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AccountsTest(APITestCase):
    client = APIClient()

    def test_register(self):
        url = reverse('register')
        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(misc)
        name = fake.user_name()
        email = fake.email()
        password = fake.password(length=8)
        data = {
            'username': name, 
            'email': email, 
            'password1': password,
            'password2': password
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = reverse('login')
        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(misc)
        name = fake.user_name()
        email = fake.email()
        password = fake.password(length=8)
        user = User.objects.create_user(name, email, password)
        data = {
            'email': email,
            'password': password
        }
        response = self.client.post(url, data, format='json')
        token = Token.objects.get(user=user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(f'{response.data["key"]}', f'{token}')

    def test_logout(self):
        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(misc)
        name = fake.user_name()
        email = fake.email()
        password = fake.password(length=8)
        user = User.objects.create_user(name, email, password)
        data = {
            'email': email,
            'password': password
        }
        url = reverse('login')
        self.client.post(url, data, format='json')
        url = reverse('logout')
        token = Token.objects.get(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Token.objects.filter(user=user).exists(), False)
