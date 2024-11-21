from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Attendance
from .serializers import AttendanceSerializer, CreateAttendanceSerializer
from users.permissions import IsTeacher, IsAdmin

class AttendanceView(APIView):
    permission_classes = [IsAuthenticated & (IsTeacher | IsAdmin)]

    def get(self, request):
        # Teachers can view attendance for their courses, Admins can view all
        if request.user.role == 'teacher':
            attendance_records = Attendance.objects.filter(course__instructor=request.user)
        elif request.user.role == 'admin':
            attendance_records = Attendance.objects.all()
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        serializer = AttendanceSerializer(attendance_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Attendance record created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttendanceForStudentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Students can view their own attendance records
        if request.user.role == 'student':
            attendance_records = Attendance.objects.filter(student=request.user)
            serializer = AttendanceSerializer(attendance_records, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
