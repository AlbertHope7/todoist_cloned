from rest_framework import serializers

from todos.models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "id",
            "task",
            "description",
            "created_at",
            "due_until",
        ]
