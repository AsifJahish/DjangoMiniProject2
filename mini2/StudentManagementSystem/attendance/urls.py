from django.urls import path
from .views import AttendanceView, AttendanceForStudentView

urlpatterns = [
    path('records/', AttendanceView.as_view(), name='attendance_records'),
    path('student/', AttendanceForStudentView.as_view(), name='student_attendance'),
]
