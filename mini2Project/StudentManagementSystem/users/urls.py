from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    register, user_login, user_logout, profile, 
    UserViewSet, UserAPIView
) 
from students.views import student_dashboard

# Router for ViewSet
router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

# URL patterns for templates
urlpatterns = [
    # Template URLs
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    
    # API URLs
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user/', UserAPIView.as_view(), name='user-api'),
]