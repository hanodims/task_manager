from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter 
from rest_framework import exceptions


from datetime import datetime

from .models import Board, Task
from .permissions import IsBoardOwner,IsOwner
from .serializers import CreateBoardSerializer,BoardSerializer,UserBoardSerializer,CreateTaskSerializer,HideTaskSerializer,TaskListSerializer,BoardTaskListSerializer


class CreateBoard(CreateAPIView):
    serializer_class = CreateBoardSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DeleteBoard(DestroyAPIView):
	queryset = Board.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'board_id'
	permission_classes = [IsBoardOwner]


class ListBoard(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated]


class UserListBoard(ListAPIView):
    serializer_class = UserBoardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)


class CreateTask(CreateAPIView):
    serializer_class = CreateTaskSerializer
  
    def perform_create(self, serializer):
        board_id = self.kwargs['board_id'] 
        board_obj = Board.objects.get(id=board_id)
        if board_obj.owner == self.request.user:
            return serializer.save(board=board_obj)
        else:
            raise exceptions.ParseError({"error":["Not Your Board"]})


class HideTask(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class= HideTaskSerializer
    permission_classes = [IsOwner]
    lookup_field = 'id'
    lookup_url_kwarg = 'task_id'


class DeleteTask(DestroyAPIView):
	queryset = Task.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'task_id'
	permission_classes = [IsOwner]


class ListBoardTask(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardTaskListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'board_id'
    permission_classes = [IsBoardOwner]
    #filter_backends = [OrderingFilter]

