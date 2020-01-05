from .models import Task
from rest_framework import serializers
from backend.profiles.models import Profile


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["name", "due_date", "is_done"]


class TaskToDoSerializer(serializers.ModelSerializer):
    # , queryset=Task.objects.filter(is_done=False))
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ('tasks',)

# class TaskDoneSerializer(serializers.ModelSerializer):
#     tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True, queryset=Task.objects.filter(is_done=True))
#     class Meta:
#         model=Profile
#         fields = ('tasks',)
