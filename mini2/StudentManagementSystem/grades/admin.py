from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Grade

if not admin.site.is_registered(Grade):
    admin.site.register(Grade)