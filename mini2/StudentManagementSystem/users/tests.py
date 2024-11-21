from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status

User = get_user_model()

class UserTests(APITestCase):
    def test_register_user(self):
        data = {'username': 'testuser', 'password': 'password123', 'email': 'test@test.com', 'role': 'student'}
        response = self.client.post('/api/users/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        user = User.objects.create_user(username='testuser', password='password123', email='test@test.com', role='student')
        response = self.client.post('/api/users/login/', {'username': 'testuser', 'password': 'password123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_profile_update(self):
        user = User.objects.create_user(username='testuser', password='password123', email='test@test.com', role='student')
        self.client.force_authenticate(user=user)
        response = self.client.put('/api/users/me/', {'first_name': 'NewName'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
