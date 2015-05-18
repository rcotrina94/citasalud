# coding=utf-8

from rest_framework import serializers
from citasalud.apps.main.models import PerfilUsuario, Medico, Especialidad
from django.contrib.auth.models import User


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    """ Serializador para Perfil de Usuario """
    
    class Meta:
        model = PerfilUsuario


class UsuarioSerializer(serializers.ModelSerializer):
    profile = PerfilUsuarioSerializer()

    class Meta:
        model = User
        fields = ('username', 'email', 'profile', 'is_active')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class MedicoSerializer(serializers.ModelSerializer):
    """ Serializador para Médico """

    class Meta:
        model = Medico
        # extra_kwargs = {'password': {'write_only': True}}


class EspecialidadSerializer(serializers.ModelSerializer):
    """ Serializador para Especialidad """

    class Meta:
        model = Especialidad
        fields = ('id', 'nombre')
