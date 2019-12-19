from django.db import models
from backend.core.models import TimestampedModel
from backend.profiles.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class Task(TimestampedModel):
    name = models.CharField(max_length=20)
    description = models.TextField()
    due_date = models.DateField()
    is_done = models.BooleanField()
    # Foreign Keys
    kind = models.ForeignKey("Kind", on_delete=models.PROTECT)
    assignee = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="tasks_created")
    author = models.ForeignKey(
        Profile, on_delete=models.SET_DEFAULT, related_name="tasks_todo", default=models.F('assignee'))

    def __str__(self):
        return self.name


class Subtask(TimestampedModel):
    name = models.CharField(max_length=20)
    description = models.TextField()
    place = models.SmallIntegerField()
    parent = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Kind(TimestampedModel):
    name = models.CharField(max_length=15)
    author = models.ForeignKey(to='profiles.Profile', on_delete=models.CASCADE)
    importance = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.name
