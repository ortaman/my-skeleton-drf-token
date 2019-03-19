
import json

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient


class CreateUserWithoutAuthTest(APITestCase):
    user = {
        "email": "user1@user.com",
        "username": "username1",
        "password": "pass",
        "names": "name1",
        "surnames": "surname1",
        "phone": "11111111",
        "gender": "femenino"
    }

    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        response = self.client.post(
            '/api/v1/user/',
            data=json.dumps(self.user),
            content_type='application/json'
        )

        self.assertIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_user(self):
        self.test_create_user()

        response = self.client.get('/api/v1/user/1/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user(self):
        self.test_create_user()

        response = self.client.put('/api/v1/user/1/', data='{}', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserWithAdminAuthTest(APITestCase):
    fixtures = ['users.json']

    def setUp(self):
        token = Token.objects.get(user__username='admin')

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_retrieve_user(self):
        response = self.client.get(
            '/api/v1/user/1/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.data,
            {
                'id': 1,
                "email": "admin@admin.com",
                "username": "admin",
                "names": "name",
                "surnames": "surname",
                "phone": "1111111111",
                "gender": "femenino"
            }
        )

    def test_update_user(self):

        data = {
                'id': 1,
                "email": "admin_updated@admin.com",
                "username": "admin_updated",
                "password": "pass",
                "names": "name_updated",
                "surnames": "surname_update",
                "phone": "222222222",
                "gender": "masculino"
            }

        # test update to self
        response = self.client.put(
            '/api/v1/user/1/',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.data,
            {
                'id': 1,
                "email": "admin_updated@admin.com",
                "username": "admin_updated",
                "names": "name_updated",
                "surnames": "surname_update",
                "phone": "222222222",
                "gender": "masculino"
            }
        )

        # test update to another user
        response = self.client.put(
            '/api/v1/user/2/',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertDictEqual(
            response.data,
            {'detail': 'You do not have permission to perform this action.'}
        )


class UserWithAuthTest(APITestCase):
    fixtures = ['users.json']

    def setUp(self):
        token = Token.objects.get(user__username='username')

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_retrieve_user(self):
        response = self.client.get(
            '/api/v1/user/2/',
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.data,
            {
                'id': 2,
                "email": "user@user.com",
                "username": "username",
                "names": "name",
                "surnames": "surname",
                "phone": "2222222222",
                "gender": "femenino"
            }
        )

    def test_update(self):

        data = {
                'id': 2,
                "email": "user_updated@user.com",
                "username": "username_updated",
                "password": "pass",
                "names": "name_updated",
                "surnames": "surname_update",
                "phone": "222222222",
                "gender": "masculino"
            }

        # test update to itself
        response = self.client.put(
            '/api/v1/user/2/',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.data,
            {
                'id': 2,
                "email": "user_updated@user.com",
                "username": "username_updated",
                "names": "name_updated",
                "surnames": "surname_update",
                "phone": "222222222",
                "gender": "masculino"
            }
        )

        # test update to another user
        response = self.client.put(
            '/api/v1/user/1/',
            data=json.dumps(data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertDictEqual(
            response.data,
            {'detail': 'You do not have permission to perform this action.'}
        )
