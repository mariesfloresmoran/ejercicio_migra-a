from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView #PARA API GET
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import status #PARA API POST PARA Q SE VEA ELEGANTE
from rest_framework.response import Response #PARA API GET
from django.shortcuts import get_object_or_404 #PARA API POST
# Create your views here.

class TaskView(ModelViewSet):
    #recibe dos cosas el queryset y dos serializer
    #permission_classes = [IsAuthenticated]  #esto bloquea la entrada a menos que tenga permiso
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

"""CRUD usando APIView - actualizar, eliminar y traer por ID requieren primary key mientras q la ruta GET y POST no usan y pueden traerlo todo"""

class TodoView(APIView):
    """APIView ya tiene get, post, put, delete, patch"""
    def get(self, request): #PARA PODERM LISTAR TODAS LAS TAREAS
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({
            "ok": True,
            "data": serializer.data
        })

    def post(self, request):
        serializer = TodoSerializer(data=request.data) #EN ESTE REQUEST ESTÁN LOS DATOS JSON

        if serializer.is_valid():
            serializer.save()

            return Response({
                "ok": True,
                "message": "TODO created"
            }, status=status.HTTP_201_CREATED)

        return Response({
            "ok": False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Realizamos otra clase para poder en base al método get_todo obtener el registro en base a su id ya que en la otra clase ya trae propio ID
class TodoViewDetail(APIView):
    """Lista por ID"""
    def get(self, request, id):
        todo = get_object_or_404(Todo, pk=id)
        serializer = TodoSerializer(todo)
        return Response({
            "ok": True,
            "data": serializer.data
        })

    """Actualizar por ID"""
    def put(self, request, id):
        todo = get_object_or_404(Todo, pk=id) #si existe entonces retorna un objeto sino no le permite llegar al error
        serializer = TodoSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "ok": True,
                "message": "TODO updated"
            })

        return Response({
            "ok": False,
            "message": serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    """Eliminar por ID"""
    def delete(self, request, id):
        todo = get_object_or_404(Todo, pk=id) #si existe entonces continúa con el delete sino no le permite llegar al error
        todo.delete()
        return Response({
            "ok": True,
            "message": "TODO deleted"
        })