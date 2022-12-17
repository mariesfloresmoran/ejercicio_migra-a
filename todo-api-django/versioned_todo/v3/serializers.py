from rest_framework.serializers import ModelSerializer
from tasks.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"
        read_only_fields = 'created_at', 'done_at', 'updated_at', 'deleted_at'