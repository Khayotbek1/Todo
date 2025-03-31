from django.db import models
from django.db.models import SET_NULL


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    course = models.PositiveSmallIntegerField(default=1)
    number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.TextField()
    done = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} - {self.desc}"
