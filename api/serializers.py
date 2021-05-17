from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)
    tag_name = serializers.ReadOnlyField(source='tag.name', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at', 'updated_at', 'tag', 'tag_name')
