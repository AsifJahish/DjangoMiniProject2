# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import StudentViewSet

# router = DefaultRouter()
# router.register('students', StudentViewSet, basename='student')

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, student_dashboard, StudentPerformanceView

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    # Template rendering for student dashboard
    path('', student_dashboard, name='student_dashboard'),  # Student dashboard template
    
    # API URLs
    path('api/', include(router.urls)),
    path('api/student/performance/', StudentPerformanceView.as_view(), name='student-performance'),
]