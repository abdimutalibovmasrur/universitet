from django.utils import timezone
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=timezone.now)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=200, default='Male')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default='2024-12-31')
    max_student = models.PositiveIntegerField()

    def __str__(self):
        return self.title
