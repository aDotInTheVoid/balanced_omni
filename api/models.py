from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=30)
    discription=models.TextField()
    due_date = models.DateField()
    subject = models.ForeignKey(Subject, null=True, on_delete=models.SET_NULL)
    importance = models.PositiveSmallIntegerField()
    urgency = models.PositiveSmallIntegerField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
