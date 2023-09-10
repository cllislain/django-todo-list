from django.urls import path

from . import views

urlpatterns = [
    path("todo-lists/", views.todo_lists, name="todo_lists"),
    path("todo-list/<int:id>/", views.todo_list_item, name="todo_list_detail"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("delete_todo_list/<int:id>/", views.delete_todo_list, name="todo_list_delete"),
]
