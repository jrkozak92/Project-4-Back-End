from django.urls import path
from . import views

urlpatterns = [
    path('api/todo', views.TodoList.as_view(), name='todo_list'),
    path('api/todo/<int:pk>', views.TodoDetail.as_view(), name='todo_detail'),
]
