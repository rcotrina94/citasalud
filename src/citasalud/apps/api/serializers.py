# coding=utf-8

from rest_framework import serializers
from citasalud.apps.main.models import Usuario, Medico, Especialidad


class MedicoSerializer(serializers.ModelSerializer):
    """ Serializador para Médico """

    class Meta:
        model = Medico


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
#        fields = ('id', 'username', 'profile','is_superuser')

    # def create(self, validated_data):
    #     profile_data = validated_data.pop('profile')
    #     user = Usuario.objects.create(**validated_data)
    #     Profile.objects.create(user=user, **profile_data)
    #     return user


class EspecialidadSerializer(serializers.ModelSerializer):
    """ Serializador para Especialidad """

    class Meta:
        model = Especialidad
        # fields = ('id', 'nombre')
