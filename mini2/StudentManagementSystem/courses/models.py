from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructed_courses', limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments', limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"

    class Meta:
        unique_together = ('student', 'course')  # Prevent duplicate enrollments
