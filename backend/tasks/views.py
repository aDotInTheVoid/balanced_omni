from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from . import permissions


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsOwner, IsAuthenticated]

    def get_queryset(self):
        return self.request.user.profile.task_set.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
