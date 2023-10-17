from django.db import models
from courses.models import Course

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, unique=True, blank=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.registration_number:
            last_registration = Student.objects.order_by('-id').first()
            if last_registration and last_registration.registration_number.startswith('ICI'):
                last_number = int(last_registration.registration_number[3:])
            else:
                last_number = 0
            new_number = last_number + 1
            self.registration_number = f'ICI{new_number:06}'
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'