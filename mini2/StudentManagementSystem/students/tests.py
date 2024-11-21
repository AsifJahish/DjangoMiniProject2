from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from .models import StudentProfile

User = get_user_model()

class StudentTests(APITestCase):
    def setUp(self):
        self.student_user = User.objects.create_user(username='student1', password='password123', role='student')
        self.admin_user = User.objects.create_user(username='admin1', password='password123', role='admin')
        self.student_profile = StudentProfile.objects.create(user=self.student_user, dob='2000-01-01')

    def test_student_view_own_profile(self):
        self.client.force_authenticate(user=self.student_user)
        response = self.client.get('/api/students/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], self.student_user.username)

    def test_admin_view_all_profiles(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get('/api/students/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_update_profile(self):
        self.client.force_authenticate(user=self.student_user)
        response = self.client.post('/api/students/profile/', {'dob': '1999-12-31'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student_profile.refresh_from_db()
        self.assertEqual(self.student_profile.dob.strftime('%Y-%m-%d'), '1999-12-31')
