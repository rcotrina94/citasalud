# coding=utf-8

from django.contrib import admin
from .models import (Usuario, Especialidad, CitaMedica, Medico,
					 Paciente, Empleado, HistoriaClinica, Examen,
					 TipoExamen,)
from django.contrib.auth.admin import UserAdmin


admin.site.register(Usuario)
admin.site.register(Especialidad)
admin.site.register(CitaMedica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Empleado)
admin.site.register(HistoriaClinica)
admin.site.register(Examen)
admin.site.register(TipoExamen)

# admin.site.register(Usuario, UsuarioAdmin)

# class PersonalAdmin(admin.ModelAdmin):
#     pass


# class PacienteAdmin(admin.ModelAdmin):
#     pass


# class MedicoAdmin(admin.ModelAdmin):
#     pass


# class CitaMedicaAdmin(admin.ModelAdmin):
#     pass
