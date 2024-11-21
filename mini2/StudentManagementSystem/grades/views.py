from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Grade
from .serializers import GradeSerializer, CreateGradeSerializer
from users.permissions import IsTeacher, IsAdmin

class GradeView(APIView):
    permission_classes = [IsAuthenticated & (IsTeacher | IsAdmin)]

    def get(self, request):
        if request.user.role == 'teacher':
            grades = Grade.objects.filter(course__instructor=request.user)
        elif request.user.role == 'admin':
            grades = Grade.objects.all()
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        serializer = GradeSerializer(grades, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CreateGradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Grade added successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentGradeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'student':
            grades = Grade.objects.filter(student=request.user)
            serializer = GradeSerializer(grades, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
