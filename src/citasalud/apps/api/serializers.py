# coding=utf-8

from rest_framework import serializers
from citasalud.apps.main.models import Usuario, Medico, Especialidad, Empleado


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ("username", "nombre", "avatar","is_active","is_superuser",)
        extra_kwargs = {
                'password': { 'write_only': True },
                'is_superuser' : { 'read_only' : True }
            }


class EspecialidadSerializer(serializers.ModelSerializer):
    """ Serializador para Especialidad """

    class Meta:
        model = Especialidad
        # fields = ('id', 'nombre')


class MedicoSerializer(serializers.ModelSerializer):
    """ Serializador para Médico """
    especialidades = EspecialidadSerializer(many=True)
    
    class Meta:
        fields = ('ncolegiado', 'departamento', 'tipo', 'especialidades', 'nombre', 'contacto')
        model = Medico
        
       
class BasicEmpleadoSerializer(serializers.ModelSerializer):
    """ Serializador Básico para Empleado """    
    usuario = UsuarioSerializer()
    class Meta:
        model = Empleado
        extra_kwargs = {'superior': { 'write_only': True }}


class EmpleadoSerializer(BasicEmpleadoSerializer):
    """ Serializador para Empleado """
    superior = BasicEmpleadoSerializer()