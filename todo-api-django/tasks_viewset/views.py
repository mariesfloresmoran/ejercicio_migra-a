# Create your views here.
#Todo y TodoSerializer debido a que ya existen no se deben crear de nuevo porque sería un error
from tasks.models import Todo
from tasks.serializers import TodoSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet #traemos el modelo ModelViewSet nos trae el CRUD entero y el ReadOnlyModelViewSet solo nos ayuda a obtener cosas
from rest_framework import filters #la tra opcion
from .pagination import SimplePagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

"""
Tenemos 2 atributos que recibe como minimo el ModelViewSet
queryset
serializer_class
"""

class TaskViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = SimplePagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title', 'body']
    search_fields = ['title', 'body']

    throttle_classes = [UserRateThrottle]

    @action(detail=True, methods=['get'], url_path="detalle", url_name="detalle")
    def detalle(self, request, pk=None):
        return self.retrieve(request, pk)

class TaskReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']