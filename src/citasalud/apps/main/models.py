# coding=utf-8
from django.db import models
from .constants import TIPO_MEDICO
from .customfields import DNIField, PrimaryNumberField
from django.contrib.auth.models import User


class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User)
    activado = models.BooleanField("Usuario activado")

    dni = DNIField("DNI", unique=True)
    nombre = models.CharField("Nombre", max_length=32)
    apellido_paterno = models.CharField("Ap. Paterno", max_length=16)
    apellido_materno = models.CharField("Ap. Materno", max_length=16)

    fecha_nacimiento = models.DateField("Fecha de Nacimiento")
    telefono = models.CharField("Teléfono", max_length=9, blank=True)

    ciudad = models.CharField("Ciudad de origen", max_length=128)

    email = models.EmailField("E-mail", unique=True, blank=True)
    avatar = models.ImageField("Imagen", upload_to="avatar", null=False, default="/media/avatar/sin_imagen.png", blank=True)

    def get_name(self):
        return self.nombre.split(" ")[0]

    def get_full_name(self):
        return "%s %s %s" % (self.nombre, self.apellido_paterno, self.apellido_materno)

    def get_short_name(self):
        return "%s %s" % (self.get_name(), self.apellido_paterno)

    def __unicode__(self):
        return "[%s] %s" % (self.dni, self.get_full_name())

    # def has_perm(self, perm, obj=None):
    #     return True

    # def has_module_perms(self, app_label):
    #     return True


class PerfilPaciente(models.Model):
    usuario = models.OneToOneField('PerfilUsuario')
    nss = PrimaryNumberField("NSS", digits=9)

    def __unicode__(self):
        return "%s, %s (%s)" % (self.apellidos, self.nombre, self.nss)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class PerfilPersonal(models.Model):
    usuario = models.OneToOneField('PerfilUsuario')
    nregistropersonal = PrimaryNumberField("N° Registro personal")
    departamento = models.CharField("Departamento", max_length=32)


class PerfilMedico(PerfilPersonal):
    ncolegiado = PrimaryNumberField("N° Colegiado")
    especialidades = models.ManyToManyField("Especialidad", blank=True, related_name='especialidades')

    @property
    def tipo(self):
        return TIPO_MEDICO.ESPECIALISTA if self.especialidades else TIPO_MEDICO.GENERAL

    def __unicode__(self):
        return "%s, %s (%s)" % (self.apellidos, self.nombre, self.ncolegiado)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        ordering = ('ncolegiado',)


class Especialidad(models.Model):
    id = models.CharField("ID Especialidad", max_length=5, primary_key=True)
    nombre = models.CharField("Nombre", max_length=32)

    def __unicode__(self):
        return "%s - %s" % (self.id, self.nombre)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
        ordering = ('id',)


class CitaMedica(models.Model):
    historia = models.ForeignKey("HistoriaClinica")
    medico = models.ForeignKey("PerfilMedico")
    horario = models.DateTimeField("Hora de cita")
    asistio = models.BooleanField()

    class Meta:
        verbose_name = u"Cita médica"
        verbose_name_plural = "Citas médicas"


class HistoriaClinica(models.Model):
    paciente = models.OneToOneField("PerfilPaciente")