from django.shortcuts import render
from rest_framework import viewsets

from todo.articledb import article
from todo.models import Todo, TodoList
from todo.serializers import TodoSerializer, TodoListSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListViewset(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


def index(request):
    context = {
        "article": article,
    }
    return render(request, 'index.html', context)
