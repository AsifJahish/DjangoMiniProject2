from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Course, Enrollment

User = get_user_model()

class CoursesTests(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher1', password='password123', role='teacher')
        self.student = User.objects.create_user(username='student1', password='password123', role='student')
        self.course = Course.objects.create(name='Math', description='Math Course', instructor=self.teacher)

    def test_teacher_view_courses(self):
        self.client.force_authenticate(user=self.teacher)
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_student_enroll_in_course(self):
        self.client.force_authenticate(user=self.teacher)
        data = {'student': self.student.id, 'course': self.course.id}
        response = self.client.post('/api/courses/enrollments/', data)
        self.assertEqual(response.status_code, 201)
