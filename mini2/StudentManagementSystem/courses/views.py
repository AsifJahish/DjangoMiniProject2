from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Course, Enrollment
from .serializers import CourseSerializer, CreateCourseSerializer, EnrollmentSerializer, CreateEnrollmentSerializer
from users.permissions import IsAdmin, IsTeacher

class CourseView(APIView):
    permission_classes = [IsAuthenticated & (IsTeacher | IsAdmin)]

    def get(self, request):
        if request.user.role == 'teacher':
            courses = Course.objects.filter(instructor=request.user)
        elif request.user.role == 'admin':
            courses = Course.objects.all()
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Course created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'student':
            enrollments = Enrollment.objects.filter(student=request.user)
        elif request.user.role == 'teacher':
            enrollments = Enrollment.objects.filter(course__instructor=request.user)
        elif request.user.role == 'admin':
            enrollments = Enrollment.objects.all()
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateEnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Student enrolled successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
