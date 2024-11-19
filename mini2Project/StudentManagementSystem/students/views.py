from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action  # Import action decorator
from .models import Student
from .serializers import StudentSerializer, StudentListSerializer
from rest_framework.views import APIView
from django.db.models import Avg
from users.permissions import IsAdminUser, IsTeacherUser, IsStudentUser
import logging

# Configure logger
logger = logging.getLogger(__name__)

# Template rendering student dashboard
def student_dashboard(request):
    """
    Render the student dashboard page, displaying data.
    """
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None
    
    return render(request, 'student_dashboard.html', {'student': student})


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email', 'student_id']
    ordering_fields = ['name', 'registration_date']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action == 'list':
            return StudentListSerializer
        return StudentSerializer

    def get_permissions(self):
        # Fix permission assignment
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser, IsTeacherUser]  # Use a list of permissions
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        if self.request.user.role == 'student':
            return Student.objects.filter(user=self.request.user)
        return self.queryset

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        cache_key = f'student_profile_{instance.id}'
        cached_data = cache.get(cache_key)
        
        if cached_data is None:
            serializer = self.get_serializer(instance)
            cached_data = serializer.data
            cache.set(cache_key, cached_data, timeout=60*15)  # Cache for 15 minutes
        
        return Response(cached_data)

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        student = self.get_object()
        grades = student.grades.all()
        attendance = student.attendance_records.all()
        
        # Calculate performance metrics
        performance_data = {
            'average_grade': grades.aggregate(Avg('grade'))['grade__avg'],
            'attendance_rate': attendance.filter(status='present').count() / attendance.count() * 100 if attendance.count() > 0 else 0,
            'total_courses': student.enrollments.count(),
        }
        
        return Response(performance_data)

    def perform_create(self, serializer):
        logger.info(f"Creating new student record by {self.request.user}")
        serializer.save()

    def perform_update(self, serializer):
        logger.info(f"Updating student record {serializer.instance.student_id} by {self.request.user}")
        serializer.save()


# API view to fetch student performance data
class StudentPerformanceView(APIView):
    """
    API view to fetch student performance details.
    """
    permission_classes = [IsAuthenticated, IsStudentUser]  # Fixed permission classes

    def get(self, request):
        student = Student.objects.get(user=request.user)
        performance_data = {
            'average_grade': student.grades.aggregate(Avg('grade'))['grade__avg'],
            'attendance_rate': student.attendance_records.filter(status='present').count() / student.attendance_records.count() * 100,
            'total_courses': student.enrollments.count(),
        }
        return Response(performance_data)
