from django.db import models

from backend.core.models import TimestampedModel
from backend.profiles.models import Profile

class Task(TimestampedModel):
    name = models.CharField(max_length=20)
    due_date = models.DateField()
    is_done = models.BooleanField()   
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

