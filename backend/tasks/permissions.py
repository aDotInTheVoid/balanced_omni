from django.contrib.auth.models import AnonymousUser

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if isinstance(request.user, AnonymousUser):
            return False
        else:
            return obj.author == request.user.profile
