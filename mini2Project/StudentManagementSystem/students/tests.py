from django.test import TestCase

# Create your tests here.
# students/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Student
from datetime import date

User = get_user_model()

class StudentModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            role='student'
        )
        
        self.student = Student.objects.create(
            user=self.user,
            name='Test Student',
            email='test@example.com',
            date_of_birth=date(2000, 1, 1),
            address='Test Address',
            phone_number='1234567890',
            student_id='ST001'
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, 'Test Student')
        self.assertEqual(self.student.student_id, 'ST001')
        self.assertTrue(isinstance(self.student, Student))
        self.assertEqual(str(self.student), 'Test Student (ST001)')

class StudentAPITests(APITestCase):
    def setUp(self):
        # Create admin user
        self.admin_user = User.objects.create_user(
            email='admin@example.com',
            password='admin123',
            role='admin',
            is_staff=True
        )
        
        # Create teacher user
        self.teacher_user = User.objects.create_user(
            email='teacher@example.com',
            password='teacher123',
            role='teacher'
        )
        
        # Create student user
        self.student_user = User.objects.create_user(
            email='student@example.com',
            password='student123',
            role='student'
        )
        
        # Create student profile
        self.student = Student.objects.create(
            user=self.student_user,
            name='Test Student',
            email='student@example.com',
            date_of_birth=date(2000, 1, 1),
            address='Test Address',
            phone_number='1234567890',
            student_id='ST001'
        )

    def test_list_students_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_students_teacher(self):
        self.client.force_authenticate(user=self.teacher_user)
        response = self.client.get(reverse('student-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_can_view_own_profile(self):
        self.client.force_authenticate(user=self.student_user)
        response = self.client.get(
            reverse('student-detail', kwargs={'pk': self.student.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['student_id'], 'ST001')

    def test_student_cannot_view_other_profiles(self):
        other_student = Student.objects.create(
            user=User.objects.create_user(
                email='other@example.com',
                password='other123',
                role='student'
            ),
            name='Other Student',
            email='other@example.com',
            date_of_birth=date(2000, 1, 1),
            address='Other Address',
            phone_number='0987654321',
            student_id='ST002'
        )
        
        self.client.force_authenticate(user=self.student_user)
        response = self.client.get(
            reverse('student-detail', kwargs={'pk': other_student.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_admin_can_create_student(self):
        self.client.force_authenticate(user=self.admin_user)
        data = {
            'user': User.objects.create_user(
                email='new@example.com',
                password='new123',
                role='student'
            ).id,
            'name': 'New Student',
            'email': 'new@example.com',
            'date_of_birth': '2000-01-01',
            'address': 'New Address',
            'phone_number': '1231231234',
            'student_id': 'ST003'
        }
        response = self.client.post(reverse('student-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_cannot_create_profile(self):
        self.client.force_authenticate(user=self.student_user)
        data = {
            'name': 'New Student',
            'email': 'new@example.com',
            'date_of_birth': '2000-01-01',
            'student_id': 'ST003'
        }
        response = self.client.post(reverse('student-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_cache_behavior(self):
        self.client.force_authenticate(user=self.admin_user)
        # First request - should hit the database
        response1 = self.client.get(
            reverse('student-detail', kwargs={'pk': self.student.pk})
        )
        # Second request - should hit the cache
        response2 = self.client.get(
            reverse('student-detail', kwargs={'pk': self.student.pk})
        )
        self.assertEqual(response1.data, response2.data)