from rest_framework import routers
from todo.views import TodoViewset,TodoListViewset

router = routers.DefaultRouter()
router.register('todos',TodoViewset)
router.register('todos-list',TodoListViewset)
