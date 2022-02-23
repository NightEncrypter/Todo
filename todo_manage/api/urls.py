from django.urls import path
from . import views
urlpatterns=[
    path("test",views.test,name="test"),
    path("todo/<str:pk>",views.getTodo,name="gettodo"),
    path("todos",views.getTodos,name="gettodos"),
    path("create",views.createTodo,name="create"),
    path("delete/<str:pk>",views.deleteTodo,name="delete"),
    path("update/<str:pk>",views.updateTodo,name="update"),
]