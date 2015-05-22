# coding=utf-8
from django.db import models
from .constants import TIPO_MEDICO
from .customfields import DNIField, PrimaryNumberField
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UsuarioManager(BaseUserManager):
    def create_user(self, dni,fecha_nacimiento, nombres,apellido_paterno,password =None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not dni:
            raise ValueError('EL USUARIO DEBE TENER DNI')

        user = self.model(
             dni=dni,
             nombres=nombres,
             apellido_paterno=apellido_paterno,
             fecha_nacimiento=fecha_nacimiento
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, dni,fecha_nacimiento, nombres,apellido_paterno,password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(dni,
            password=password,
             nombres=nombres,
             apellido_paterno=apellido_paterno,
             fecha_nacimiento=fecha_nacimiento
        )
        user.is_active=True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
#    def normalize_dni (self,dni):
    

class Usuario(AbstractBaseUser):
    dni = DNIField("DNI", unique=True , primary_key= True )
    nombre = models.CharField("Nombre", max_length=32)
    apellido_paterno = models.CharField("Ap. Paterno", max_length=16)
    apellido_materno = models.CharField("Ap. Materno", max_length=16)

    fecha_nacimiento = models.DateField("Fecha de Nacimiento")
    telefono = models.CharField("Teléfono", max_length=9, blank=True)

    ciudad = models.CharField("Ciudad de origen", max_length=128)

    email = models.EmailField("E-mail", unique=True, blank=True)
    avatar = models.ImageField("Imagen", upload_to="avatar", null=False, default="/media/avatar/sin_imagen.png", blank=True)
    
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default = False)
    
    objects=UsuarioManager()
    
    USERNAME_FIELDS= 'dni'
    REQUIRED_FIELDS = [ 'fecha_nacimiento','nombres' ,'apellido_paterno' ]

    def get_name(self):
        return self.nombre.split(" ")[0]

    def get_full_name(self):
        return "%s %s %s" % (self.nombre, self.apellido_paterno, self.apellido_materno)

    def get_short_name(self):
        return "%s %s" % (self.get_name(), self.apellido_paterno)

    def __unicode__(self):
        return "[%s] %s" % (self.dni, self.get_full_name())

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

#    def has_perm(self, perm, obj=None):
#        #"Does the user have a specific permission?"
#        # Simplest possible answer: Yes, always
#        return True
#
#    def has_module_perms(self, app_label):
#        "Does the user have permissions to view the app `app_label`?"
#        # Simplest possible answer: Yes, always
#        return True


class Paciente(models.Model):
    usuario = models.ForeignKey(Usuario, unique=True, related_name="paciente")
    nss = PrimaryNumberField("NSS", digits=9)

    def __unicode__(self):
        return "%s (%s)" % (self.usuario.get_short_name(), self.nss)

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


class Personal(models.Model):
    usuario = models.ForeignKey(User, unique=True, related_name="personal")
    nregistropersonal = PrimaryNumberField("N° Registro personal")
    departamento = models.CharField("Departamento", max_length=32)
    
#    class Meta:
#        proxy = True


class Medico(Personal):
    ncolegiado = PrimaryNumberField("N° Colegiado")
    especialidades = models.ManyToManyField("Especialidad", blank=True, related_name='especialidades')

    def _tipo(self):
        return TIPO_MEDICO.ESPECIALISTA if self.especialidades else TIPO_MEDICO.GENERAL
    tipo = property(_tipo)

    def __unicode__(self):
        return "%s (%s)" % (self.usuario.get_short_name(), self.ncolegiado)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"
        ordering = ('ncolegiado',)


class Especialidad(models.Model):
    id = models.CharField("ID Especialidad", max_length=5, primary_key=True)
    nombre = models.CharField("Nombre", max_length=64)

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

    
class HistoriaClinica(models.Model):
    paciente = models.ForeignKey("Paciente", unique=True)