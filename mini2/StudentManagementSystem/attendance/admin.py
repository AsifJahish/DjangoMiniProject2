from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Attendance

if not admin.site.is_registered(Attendance):
    admin.site.register(Attendance)
