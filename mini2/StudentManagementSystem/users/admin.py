from django.contrib import admin

from django.contrib import admin
from .models import User

if not admin.site.is_registered(User):
    admin.site.register(User)
