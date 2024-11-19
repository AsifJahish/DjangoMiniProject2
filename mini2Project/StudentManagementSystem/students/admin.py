from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'student_id', 'registration_date']
    search_fields = ['name', 'email', 'student_id']
    list_filter = ['registration_date']
    readonly_fields = ['registration_date']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.role == 'teacher':
            return qs.filter(courses__teacher=request.user)
        return qs.none()