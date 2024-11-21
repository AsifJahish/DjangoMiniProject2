from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from courses.models import Course

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades', limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.CharField(max_length=10)  # Example: A, B, C, or numerical grade
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.grade} in {self.course.name}"

    class Meta:
        unique_together = ('student', 'course', 'date')  # Prevent duplicate grades for the same course and date
