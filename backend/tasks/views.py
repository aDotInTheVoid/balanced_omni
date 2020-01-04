from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer
from . import permissions


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsOwner, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
