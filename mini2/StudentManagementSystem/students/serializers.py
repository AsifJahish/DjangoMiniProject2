from rest_framework import serializers
from .models import StudentProfile
from users.serializers import UserSerializer

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer for user details

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'dob', 'registration_date']

class CreateStudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['dob']
