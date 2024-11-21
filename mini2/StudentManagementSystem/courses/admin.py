from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  Course
from .models import  Enrollment

if not admin.site.is_registered(Course):
    admin.site.register(Course)


if not admin.site.is_registered(Enrollment):
    admin.site.register(Enrollment)
