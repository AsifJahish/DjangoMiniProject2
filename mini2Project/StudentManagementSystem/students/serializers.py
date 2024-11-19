
# students/serializers.py
from rest_framework import serializers
from .models import Student
from courses.serializers import EnrollmentSerializer
from grades.serializers import GradeSerializer
from attendance.serializers import AttendanceSerializer

class StudentSerializer(serializers.ModelSerializer):
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    grades = GradeSerializer(many=True, read_only=True)
    attendance_records = AttendanceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = [
            'id', 'user', 'name', 'email', 'date_of_birth', 
            'registration_date', 'address', 'phone_number', 
            'student_id', 'enrollments', 'grades', 'attendance_records'
        ]
        read_only_fields = ['registration_date']

class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'student_id']