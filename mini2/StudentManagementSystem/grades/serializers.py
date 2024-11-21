from rest_framework import serializers
from .models import Grade
from users.serializers import UserSerializer
from courses.serializers import CourseSerializer

class GradeSerializer(serializers.ModelSerializer):
    student = UserSerializer()  # Nested serializer for student details
    course = CourseSerializer()  # Nested serializer for course details

    class Meta:
        model = Grade
        fields = ['id', 'student', 'course', 'grade', 'date']

class CreateGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['student', 'course', 'grade']
