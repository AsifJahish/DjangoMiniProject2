from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import StudentProfile
from .serializers import StudentProfileSerializer, CreateStudentProfileSerializer
from users.permissions import IsStudent, IsAdmin

class StudentProfileView(APIView):
    permission_classes = [IsAuthenticated & (IsStudent | IsAdmin)]

    def get(self, request):
        if request.user.role == 'student':
            # Student can only view their own profile
            try:
                profile = StudentProfile.objects.get(user=request.user)
                serializer = StudentProfileSerializer(profile)
                return Response(serializer.data)
            except StudentProfile.DoesNotExist:
                return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        elif request.user.role == 'admin':
            # Admin can view all student profiles
            profiles = StudentProfile.objects.all()
            serializer = StudentProfileSerializer(profiles, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Admin or student can create/update profile
        if request.user.role == 'student':
            try:
                profile = StudentProfile.objects.get(user=request.user)
                serializer = CreateStudentProfileSerializer(profile, data=request.data, partial=True)
            except StudentProfile.DoesNotExist:
                serializer = CreateStudentProfileSerializer(data=request.data)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            profile = serializer.save(user=request.user)
            return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
