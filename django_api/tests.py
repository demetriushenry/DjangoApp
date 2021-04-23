from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_superuser(
            'demetrius', '1234567'
        )
        cls.id = cls.user.id

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        token = RefreshToken.for_user(self.user).access_token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_user_list(self):
        url = '/api/users/'
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, 'request goes wrong!')
        result = len(response.json())
        self.assertTrue(result > 0, 'user list is empty')

    def test_get_user(self):
        url = f'/api/users/{self.id}/'
        response = self.client.get(url)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, 'request goes wrong!')
        self.assertEqual(
            response.json()['name'],
            'demetrius',
            'user not found!'
        )

    def test_create_new_user(self):
        url = '/api/users/'
        body = {
            "name": "miguel",
            "birthday": "2014-06-24",
            "cpf": "75816148249",
            "cep": "",
            "street": "",
            "neighborhood": "",
            "city": "",
            "state": ""
        }
        response = self.client.post(url, body, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            'request goes wrong!'
        )
        self.assertEqual(
            response.json()['name'],
            'miguel',
            'create request goes wrong!'
        )

    def test_update_user(self):
        url = f'/api/users/{self.id}/'
        body = {
            "cep": "69000000",
            "street": "",
            "neighborhood": "",
            "city": "",
            "state": ""
        }
        response = self.client.patch(url, body, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            'request goes wrong!'
        )
        self.assertEqual(
            response.json()['cep'],
            '69000000',
            'update request goes wrong!'
        )

    def test_delete_user(self):
        # create a new user before deleting
        user = User.objects.create_user(
            'henry', '1234567', cpf='07812892204'
        )
        id = user.id
        # delete user
        url = f'/api/users/{id}/'
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
            'delete request goes wrong!'
        )
