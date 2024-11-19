
# students/filters.py
from django_filters import rest_framework as filters
from .models import Student

class StudentFilter(filters.FilterSet):
    registration_date_after = filters.DateFilter(field_name="registration_date", lookup_expr='gte')
    registration_date_before = filters.DateFilter(field_name="registration_date", lookup_expr='lte')
    
    class Meta:
        model = Student
        fields = {
            'name': ['exact', 'icontains'],
            'email': ['exact', 'icontains'],
            'student_id': ['exact'],
            'registration_date': ['exact', 'year', 'month'],
        }