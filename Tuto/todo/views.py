from django.shortcuts import render
from rest_framework import viewsets
from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer

class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer    
