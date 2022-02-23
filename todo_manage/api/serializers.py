

from rest_framework.serializers import ModelSerializer

from todo_manage.models import Todo

class TodosSerialized(ModelSerializer):
    class Meta:
     model=Todo
     fields="__all__"