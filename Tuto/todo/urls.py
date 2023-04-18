"""
from rest_framework import routers
from todo.views import TodoViewset,TodoListViewset

router = routers.DefaultRouter()
router.register('todos',TodoViewset)
router.register('todos-list',TodoListViewset)
"""
from django.urls import path

from todo.views import index

urlpatterns = [
    path('', index, name="index")
    # path('', include(router.urls)),

]
