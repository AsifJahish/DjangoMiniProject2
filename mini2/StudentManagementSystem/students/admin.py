from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  StudentProfile

if not admin.site.is_registered(StudentProfile):
    admin.site.register( StudentProfile)
