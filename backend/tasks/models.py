from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from backend.core.models import TimestampedModel
from backend.profiles.models import Profile

validators = [
    MinValueValidator(-5),
    MaxValueValidator(5)
]


class Task(TimestampedModel):
    name = models.CharField(max_length=20)
    due_date = models.DateField()
    is_done = models.BooleanField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    priority = models.SmallIntegerField(validators=validators)
    importance = models.SmallIntegerField(validators=validators)

    def __str__(self):
        return self.name
