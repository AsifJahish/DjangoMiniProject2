from rest_framework import serializers
from .models import Course, Enrollment
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer()  # Display instructor details

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'instructor']

class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'description', 'instructor']

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()  # Display student username
    course = serializers.StringRelatedField()  # Display course name

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrollment_date']

class CreateEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
