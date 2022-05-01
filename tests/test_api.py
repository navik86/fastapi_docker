from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web_app
from app.config import DATABASE_URL


class APITestCase(TestCase):

    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def test_create_user(self):
        user_data = {
            'user': {
                'email': 'test8@test.com',
                'password': '1234',
                'first_name': 'John',
                'last_name': 'Doe',
                'nick_name': 'joy123'
            }
        }

        response = self.client.post('/user', json=user_data)
        self.assertEqual(response.status_code, 200)