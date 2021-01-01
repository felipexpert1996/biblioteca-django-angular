from rest_framework.test import APITestCase, APIClient
from faker import Faker
from django.urls import reverse
from rest_framework import status
from faker.providers import internet, misc


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