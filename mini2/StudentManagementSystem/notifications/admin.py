from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Notification

if not admin.site.is_registered(Notification):
    admin.site.register(Notification)