# coding=utf-8
from django.db import models

from django.forms import ValidationError
from django.core.validators import EMPTY_VALUES

# from localflavor.pe.forms import PEDNIField, PERegionSelect


class DNIField(models.CharField):

    default_error_messages = {
        'invalid': (u'No es un número de DNI válido'),
        'wrong_digits': (u'Ingrese los 8 dígitos del DNI'),
    }

    def to_python(self, value):
        """
        Value must be a string in the XXXXXXXX formats.
        """

        if value in EMPTY_VALUES:
            return ''
        if not value.isdigit():
            raise ValidationError(self.error_messages['invalid'])
        if len(value) != 8:
            raise ValidationError(self.error_messages['wrong_digits'])

        return value

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        # kwargs['min_length'] = 8
        super(DNIField, self).__init__(*args, **kwargs)
        # self.max_length = 8
        # self.min_length = 8


def PrimaryNumberField(name, digits=9):
    return models.DecimalField(name, primary_key=True, max_digits=digits, decimal_places=0)
