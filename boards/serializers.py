from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Board, Task


class CreateBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title']


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title','owner']


class UserBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description','is_hidden','is_done']


class HideTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['is_hidden']


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description','creation_date']


class BoardTaskListSerializer(serializers.ModelSerializer):
    Done = serializers.SerializerMethodField()
    NotDone = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = ['title','Done','NotDone']

    def get_Done(self, obj):
        task_objs = Task.objects.filter(board=obj,is_done=True).order_by('-creation_date')
        tasks_json = TaskListSerializer(task_objs, many=True).data
        return tasks_json 

    def get_NotDone(self, obj):
        task_objs = Task.objects.filter(board=obj,is_done=False)
        tasks_json = TaskListSerializer(task_objs, many=True).data
        return tasks_json 