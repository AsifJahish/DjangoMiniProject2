from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from courses.models import Course
from .models import Attendance

User = get_user_model()

class AttendanceTests(APITestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher1', password='password123', role='teacher')
        self.student = User.objects.create_user(username='student1', password='password123', role='student')
        self.course = Course.objects.create(name='Math', description='Math Course', instructor=self.teacher)
        self.attendance = Attendance.objects.create(student=self.student, course=self.course, date='2024-11-20', status='present')

    def test_teacher_view_attendance(self):
        self.client.force_authenticate(user=self.teacher)
        response = self.client.get('/api/attendance/records/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_student_view_own_attendance(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get('/api/attendance/student/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_attendance(self):
        self.client.force_authenticate(user=self.teacher)
        data = {'student': self.student.id, 'course': self.course.id, 'date': '2024-11-21', 'status': 'absent'}
        response = self.client.post('/api/attendance/records/', data)
        self.assertEqual(response.status_code, 201)
