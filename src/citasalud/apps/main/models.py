# coding=utf-8
from django.db import models
from .constants import TIPO_MEDICO_ESPECIALISTA, TIPO_MEDICO_GENERAL
from .customfields import DNIField, PrimaryNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, username, dni, fecha_nacimiento, first_name, last_name, password=None):
        """
        """
        if not dni:
            raise ValueError('Ingrese un n° DNI válido.')

        user = self.model(
            username=username,
            dni=dni,
            first_name=first_name,
            last_name=last_name,
            fecha_nacimiento=fecha_nacimiento
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, dni, fecha_nacimiento, first_name, last_name, password):
        """
        """
        user = self.create_user(
            username,
            dni=dni,
            password=password,
            first_name=first_name,
            last_name=last_name,
            fecha_nacimiento=fecha_nacimiento
        )
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    dni = DNIField("DNI", unique=True, primary_key=True)
    username = models.CharField("Nombre de usuario", max_length=16, unique=True)
    first_name = models.CharField("Nombres", max_length=32)
    last_name = models.CharField("Ap. Paterno", max_length=16)
    apellido_materno = models.CharField("Ap. Materno", max_length=16)

    fecha_nacimiento = models.DateField("Fecha de Nacimiento")
    telefono = models.CharField("Teléfono", max_length=9, blank=True)

    ciudad = models.CharField("Ciudad de origen", max_length=128)

    email = models.EmailField("E-mail", unique=True, blank=True, null=True)
    avatar = models.ImageField("Imagen", upload_to="avatar", null=False, default="/media/avatar/sin_imagen.png", blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['dni', 'fecha_nacimiento', 'first_name', 'last_name']

    @property
    def nombre(self):
        return self.get_short_name()
    @property
    def nombre_completo(self):
        return self.get_full_name()

    def get_name(self):
        return self.first_name.split(" ")[0]

    def get_full_name(self):
        return "%s %s %s" % (self.first_name, self.last_name, self.apellido_materno)

    def get_short_name(self):
        return "%s %s" % (self.get_name(), self.last_name)
#
#    def __unicode__(self):
#        return self


class Empleado(models.Model):
    usuario = models.OneToOneField(Usuario, unique=True, related_name="personal")
    nregistropersonal = PrimaryNumberField("N° Registro de Personal")
    departamento = models.CharField("Departamento", max_length=32)
    cargo = models.CharField("Cargo", max_length=32)
    superior = models.ForeignKey('Empleado', related_name="jefe", null=True, blank=True)

    @property
    def nombre(self):
        return self.usuario.nombre

    @property
    def contacto(self):
        return self._get_contact_info()

    def _get_contact_info(self):
        return {
            'telefono':self.usuario.telefono,
            'email':self.usuario.email
        }

    def __unicode__(self):
        return "%s (%s)" % (self.nregistropersonal, self.nombre)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"


class Medico(Empleado):
    ncolegiado = models.PositiveIntegerField("N° Colegiado")
    especialidades = models.ManyToManyField("Especialidad", blank=True, related_name='especialidades')

    @property
    def tipo(self):
        return TIPO_MEDICO_ESPECIALISTA if self.especialidades.count() else TIPO_MEDICO_GENERAL

    def __unicode__(self):
        return "%s (%s)" % (self.usuario.get_short_name(), self.ncolegiado)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        ordering = ('ncolegiado',)


class Especialidad(models.Model):
    id = models.CharField("ID Especialidad", max_length=5, primary_key=True)
    nombre = models.CharField("Nombre", max_length=128)

    def __unicode__(self):
        return "%s - %s" % (self.id, self.nombre)

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"
        ordering = ('id',)


class CitaMedica(models.Model):
    historia = models.ForeignKey("HistoriaClinica")
    medico = models.ForeignKey("Medico")
    horario = models.DateTimeField("Hora de cita")
    asistio = models.BooleanField()

    class Meta:
        verbose_name = u"Cita médica"
        verbose_name_plural = "Citas médicas"


class TipoExamen(models.Model):
    nombre = models.CharField("Examen", max_length=64)
    descripcion = models.CharField("Descripción", max_length=128)

    class Meta:
        verbose_name = "Tipo de examen"
        verbose_name_plural = "Tipos de examen"


class Resultado(models.Model):
    examen = models.ForeignKey("Examen")
    documento = models.PositiveIntegerField("N° de Documento Asociado")
    descripcion = models.CharField("Descripción", max_length=256)


class Examen(models.Model):
    fecha_solitud = models.DateField("Fecha de Solicitud")
    tipo_examen = models.ForeignKey("TipoExamen")
    fecha_aplicacion = models.DateField("Fecha de aplicación")
    observacion = models.CharField("Observacion", max_length=256)
    historia = models.ForeignKey("Paciente")

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Exámenes"


class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, unique=True, related_name="paciente")
    nss = PrimaryNumberField("NSS", digits=9)

    def __unicode__(self):
        return "%s (%s)" % (self.usuario.get_short_name(), self.nss)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class HistoriaClinica(models.Model):
    numero = models.CharField("N° H.C.", max_length=5, primary_key=True)
    paciente = models.OneToOneField("Paciente", unique=True)

    class Meta:
        verbose_name = "Historia Clínica"
        verbose_name_plural = "Historias Clínicas"
