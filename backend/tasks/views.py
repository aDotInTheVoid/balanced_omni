from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError

from .serializers import TaskSerializer
from . import permissions

# drf viewsets are made of so many mixins
# pylint: disable=too-many-ancestors


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsOwner, IsAuthenticated]

    def get_queryset(self):
        # Pull the filter request out of the URL
        filtered = self.request.query_params.get('done', None)

        if filtered is None:
            return self.request.user.profile.task_set.all()
        elif filtered[0].lower() == "t":  # TODO: Only get once
            return self.request.user.profile.task_set.filter(is_done=True)
        elif filtered[0].lower() == "f":
            return self.request.user.profile.task_set.filter(is_done=False)
        else:
            raise ParseError()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
