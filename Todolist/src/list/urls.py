from . import views
from django.urls import path


urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/update/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
]
