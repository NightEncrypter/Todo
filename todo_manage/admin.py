from turtle import title
from django.contrib import admin

from todo_manage.models import Todo
from django.contrib import admin
# Register your models here.

class RegisterTodo(admin.ModelAdmin):

    list_display=("desc","title")
    search_fields=["title","desc"]
admin.site.register(Todo,RegisterTodo)