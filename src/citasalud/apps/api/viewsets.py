from ..main.models import PerfilMedico, Especialidad
from .serializers import MedicoSerializer, EspecialidadSerializer
from rest_framework import viewsets


class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicoSerializer
    queryset = PerfilMedico.objects.all()


class EspecialidadViewSet(viewsets.ModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()
