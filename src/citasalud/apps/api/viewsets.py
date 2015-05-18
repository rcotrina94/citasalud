from ..main.models import Medico, Especialidad, User
from .serializers import UsuarioSerializer, MedicoSerializer, EspecialidadSerializer
from rest_framework import viewsets


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = User.objects.all()


class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicoSerializer
    queryset = Medico.objects.all()


class EspecialidadViewSet(viewsets.ModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()
