from rest_framework import serializers
from home.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['todo_title','todo_description','is_done','uid']
        #exclude = ['created_at']