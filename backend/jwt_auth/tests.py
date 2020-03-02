from datetime import date

# from django.db.models.deletion import ProtectedError

from rest_framework.test import APITestCase
from rest_framework.status import *

from backend.jwt_auth.models import User


class NoDbUpdateJWT(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "Username", "foo@bar.baz", "Password")

    def test_cant_use_get(self):
        resp = self.client.get('/api/auth/users/login')
        self.assertEqual(resp.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_can_login(self):
        # Main Post to login
        payload = {
            "user": {
                "email": "foo@bar.baz",
                "password": "Password"
            }
        }
        resp = self.client.post('/api/auth/users/login',
                                payload, format="json")
        # Check It's Good
        self.assertEqual(resp.status_code, HTTP_200_OK)
        token = resp.json()['user']['token']
        self.assertEqual(resp.json(), {"user": {
            "email": "foo@bar.baz",
            "username": "Username",
            'token': token
        }})
        # Check we can make calls with the token
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION=f"Token {token}")
        self.assertEqual(resp.status_code, HTTP_200_OK)
        self.assertEqual(resp.json()['user']['email'], 'foo@bar.baz')
        self.assertEqual(resp.json()['user']['username'], 'Username')
        # Bytes Test
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION=f"Token {token}".encode('utf-8'))
        self.assertEqual(resp.status_code, HTTP_200_OK)

    def test_wacko_token(self):
        # Wrong Token
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION=f"Token adfdasfdaf")
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)
        # No Token
        resp = self.client.get('/api/auth/user')
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)
        # Empty Token
        resp = self.client.get('/api/auth/user', HTTP_AUTHORIZATION="Token")
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)
        # Too Much Token
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION="Token foo bar zed")
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)
        # Wrong Token header
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION="jrr tolkien")
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)
        # Someone elses token
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION="Token eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)


class DeactivatedUser(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            "Username", "foo@bar.baz", "Password")
        self.user.is_active = False
        self.user.save()
        self.token = self.user.token

    def test_cant_login_dead_user(self):
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION=f"Token {self.token}")
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)
        self.assertEqual(
            resp.json(), {'user': {'detail': 'This user has been deactivated.'}})


class DeletedUser(APITestCase):
    def setUp(self):
        user = User.objects.create_user("Username", "foo@bar.baz", "Password")
        self.token = user.token
        user.delete()

    def test_cant_login_dead_user(self):
        resp = self.client.get(
            '/api/auth/user', HTTP_AUTHORIZATION=f"Token {self.token}")
        self.assertEqual(resp.status_code, HTTP_403_FORBIDDEN)
        self.assertEqual(
            resp.json(), {'user': {'detail': 'No user matching this token was found.'}})
