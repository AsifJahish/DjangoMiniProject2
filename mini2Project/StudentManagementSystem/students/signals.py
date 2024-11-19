from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Student

@receiver(post_save, sender=Student)
def clear_student_cache(sender, instance, **kwargs):
    cache.delete(f'student_profile_{instance.id}')
    cache.delete('all_students')

# students/apps.py
from django.apps import AppConfig

class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'

    def ready(self):
        import students.signals
