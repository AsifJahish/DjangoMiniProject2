from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from courses.models import Course
from students.models import Student

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.user.email} - {self.course.name} - {self.date} - {self.status}"
