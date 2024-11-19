from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.cache import cache

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    student_id = models.CharField(max_length=20, unique=True)
    
    def save(self, *args, **kwargs):
        # Clear cache when student data is updated
        cache.delete(f'student_profile_{self.id}')
        cache.delete('all_students')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    class Meta:
        ordering = ['name']