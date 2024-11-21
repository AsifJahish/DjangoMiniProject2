from rest_framework import serializers
from .models import Attendance
from users.serializers import UserSerializer
from courses.models import Course

class AttendanceSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()  # Display student username
    course = serializers.StringRelatedField()  # Display course name

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'course', 'date', 'status']

class CreateAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['student', 'course', 'date', 'status']
