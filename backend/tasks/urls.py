from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.TaskViewSet, 'tasks')

app_name = "tasks"

urlpatterns = [
    path('', include(router.urls)),
]
