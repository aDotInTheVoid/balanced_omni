from .models import Task, Subtask, Kind
from rest_framework.serializers import ModelSerializer


class SubtaskSerializer(ModelSerializer):
    class Meta:
        model = Subtask
        fields = ["name", "description", "place"]


class TaskSerializer(ModelSerializer):
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = ["name", "description", "due_date", "is_done", "subtasks"]
