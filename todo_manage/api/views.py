from rest_framework.response import Response
from rest_framework.decorators import api_view

from todo_manage.models import Todo
from .serializers import TodosSerialized

@api_view(["GET"])
def test(request):
    
 data=["john","jenny","Garry","Brad"]
 return (Response(data))


# LIST ITEMS
@api_view(["GET"])
def getTodos(request):
    getTodos=Todo.objects.all().order_by("-id")
    
    serialized=TodosSerialized(getTodos,many=True)
    return Response(serialized.data)

# SINGLE
@api_view(["GET"])
def getTodo(request,pk):
    getTodos=Todo.objects.get(id=pk)
    
    serialized=TodosSerialized(getTodos,many=False)
    return Response(serialized.data)


# CREATE
@api_view(["POST"])
def createTodo(request):
    
    print(request.data)
    serializer=TodosSerialized(data=request.data)
    
    if serializer.is_valid():
        # save the data
        serializer.save()
        
    return Response(serializer.data)

#delete
@api_view(["POST"])
def updateTodo(request,pk):
    
    task=Todo.objects.get(id=pk)
    serializer=TodosSerialized(instance=task,data=request.data)
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)
#delete
@api_view(["DELETE"])
def deleteTodo(request,pk):
    
    # Find todo
    todo=Todo.objects.get(id=pk)
    # And delete
    todo.delete()
    return Response("your todo is deleted")