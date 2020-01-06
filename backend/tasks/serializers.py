from .models import Task
from rest_framework import serializers
from backend.profiles.models import Profile


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["name", "due_date", "is_done", "id"]

