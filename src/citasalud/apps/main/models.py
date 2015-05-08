# coding=utf-8
from django.db import models


# def NumberField(name, digits, ):
#     return models.DecimalField(name, primary_key=True, max_digits=digits, decimal_places=0)


class Personas(models.Model):
    nombre = models.CharField("Nombre", max_length=16)
    apellidos = models.CharField("Apellidos", max_length=16)

    class Meta:
        abstract = True


class Paciente(Persona):
    nss = models.DecimalField("NSS", primary_key=True, max_digits=9, decimal_places=0)
    telefono = models.CharField("Apellidos", max_length=16)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Personal(Persona):

    class Meta:
        abstract = True

    # def __str__(self):
    #     pass




class CitaMedica(models.Model):

    class Meta:
        verbose_name = u"Cita médica"
        verbose_name_plural = "Citas médicas"

    # def __str__(self):
    #     pass
