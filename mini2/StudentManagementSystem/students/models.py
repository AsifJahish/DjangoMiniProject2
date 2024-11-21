from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    dob = models.DateField(null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
