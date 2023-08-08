from django.shortcuts import render
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
# Create your views here.
from usuariosapp.serializer import TaskSerializer
from usuariosapp.models import Task

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

@extend_schema_view(
    list = extend_schema(description='Permite obtener una lista de tareas'),
    retrieve = extend_schema(description = 'Permite obtener una tarea'),
    create= extend_schema(description = 'Permite crear una tarea'),
    update = extend_schema(description = 'Permite actualizar una tarea'),
    destroy = extend_schema(description = 'Permite eliminar una tarea'),
)
class TaskViewSet(viewsets.ModelViewSet):
    #preguntamos si tiene el token
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    queryset = Task.objects.all()