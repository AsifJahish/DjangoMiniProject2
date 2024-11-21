from django.db import models

# # Create your models here.
# from django.db import models
# from users.models import User
# from courses.models import Course

# class Attendance(models.Model):
#     student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance', limit_choices_to={'role': 'student'})
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance')
#     date = models.DateField()
#     status = models.CharField(max_length=10, choices=(('present', 'Present'), ('absent', 'Absent')))

#     def __str__(self):
#         return f"{self.student.username} was {self.status} on {self.date} for {self.course.name}"


from django.db import models
from users.models import User
from courses.models import Course

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance', limit_choices_to={'role': 'student'})
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=(('present', 'Present'), ('absent', 'Absent')))

    def __str__(self):
        return f"{self.student.username} was {self.status} on {self.date} for {self.course.name}"

    class Meta:
        unique_together = ('student', 'course', 'date')  # Ensures no duplicate records for the same date
