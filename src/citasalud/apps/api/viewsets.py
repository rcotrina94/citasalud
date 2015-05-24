from ..main.models import Medico, Especialidad, Usuario, Empleado
from .serializers import UsuarioSerializer, MedicoSerializer, EspecialidadSerializer, EmpleadoSerializer
from rest_framework import viewsets


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()


class EspecialidadViewSet(viewsets.ModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()


class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    queryset = Empleado.objects.all()
    
    