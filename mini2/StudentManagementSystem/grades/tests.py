from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from courses.models import Course
from .models import Grade

User = get_user_model()

class GradeTests(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher1', password='password123', role='teacher')
        self.student = User.objects.create_user(username='student1', password='password123', role='student')
        self.course = Course.objects.create(name='Science', description='Science Course', instructor=self.teacher)
        self.grade = Grade.objects.create(student=self.student, course=self.course, grade='A')

    def test_teacher_view_grades(self):
        self.client.force_authenticate(user=self.teacher)
        response = self.client.get('/api/grades/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_student_view_own_grades(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get('/api/grades/student/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teacher_add_grade(self):
        self.client.force_authenticate(user=self.teacher)
        data = {'student': self.student.id, 'course': self.course.id, 'grade': 'B'}
        response = self.client.post('/api/grades/', data)
        self.assertEqual(response.status_code, 201)
