# TODO: Change all of this

from rest_framework import serializers

from backend.tasks.models import Task
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    tasks = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Task.objects.all())

    class Meta:
        model = Profile
        fields = ('id', 'username', 'tasks')
        read_only_fields = ('username',)

    def get_image(self, obj):
        if obj.image:
            return obj.image

        return 'https://static.productionready.io/images/smiley-cyrus.jpg'
