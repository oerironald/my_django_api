from django.core.exceptions import ValidationError
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name

    def clean(self):
        subject_counts = self.subjects.values('id').annotate(count=models.Count('id'))
        duplicate_subjects = [subject['id'] for subject in subject_counts if subject['count'] > 1]
        if duplicate_subjects:
            raise ValidationError("A course cannot have the same subject more than once.")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.subjects.set(self.subjects.all())