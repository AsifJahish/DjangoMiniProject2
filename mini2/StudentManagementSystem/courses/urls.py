from django.urls import path
from .views import CourseView, EnrollmentView

urlpatterns = [
    path('', CourseView.as_view(), name='course_list'),
    path('enrollments/', EnrollmentView.as_view(), name='enrollment_list'),
]
