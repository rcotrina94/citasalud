# coding=utf-8

from rest_framework import serializers
from citasalud.apps.main.models import PerfilMedico, Especialidad


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class MedicoSerializer(DynamicFieldsModelSerializer):
    """ Serializador para Médico """

    class Meta:
        model = PerfilMedico
        # extra_kwargs = {'password': {'write_only': True}}


class EspecialidadSerializer(serializers.ModelSerializer):
    """ Serializador para Especialidad """

    class Meta:
        model = Especialidad
        fields = ('id', 'nombre')
