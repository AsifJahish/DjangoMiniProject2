from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from .forms import UserRegistrationForm, UserLoginForm

from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from .serializers import UserSerializer
from .forms import UserRegistrationForm, UserLoginForm
from .permissions import IsAdminUser, IsTeacherUser, IsStudentUser


from .forms import LoginForm

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsTeacherUser|IsStudentUser]
        return [permission() for permission in permission_classes]

class UserAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser|IsTeacherUser|IsStudentUser]

    def get_object(self):
        return self.request.user

# Registration view (HTML form)
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)

                # Check if the user is a student and redirect accordingly
                if user.role == 'student':  # Assuming you have a 'role' attribute in your User model
                    return redirect('student_dashboard')  # Redirect to the student dashboard
                else:
                    return redirect('home')  # Redirect to the home page for other roles (admin, teacher, etc.)

            else:
                messages.error(request, "Invalid login credentials.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Profile view (HTML, login required)
@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})

# Logout view (HTML)
def user_logout(request):
    logout(request)
    return redirect('login')
