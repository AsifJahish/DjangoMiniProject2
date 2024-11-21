from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()

class NotificationsTests(APITestCase):
    def setUp(self):
        self.student = User.objects.create_user(username='student1', password='password123', role='student')
        self.teacher = User.objects.create_user(username='teacher1', password='password123', role='teacher')
        self.notification = Notification.objects.create(recipient=self.student, title='Test Notification', message='This is a test.')

    def test_student_view_notifications(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get('/api/notifications/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teacher_create_notification(self):
        self.client.force_authenticate(user=self.teacher)
        data = {'recipient': self.student.id, 'title': 'New Grade', 'message': 'You got an A in Math.'}
        response = self.client.post('/api/notifications/create/', data)
        self.assertEqual(response.status_code, 201)

    def test_mark_notification_as_read(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.post(f'/api/notifications/{self.notification.id}/mark-read/')
        self.assertEqual(response.status_code, 200)
        self.notification.refresh_from_db()
        self.assertTrue(self.notification.is_read)
