from django.urls import path
from .views import GradeView, StudentGradeView

urlpatterns = [
    path('', GradeView.as_view(), name='grade_list'),
    path('student/', StudentGradeView.as_view(), name='student_grades'),
]
