# coding=utf-8

from django.contrib import admin
from .models import PerfilUsuario, Especialidad, CitaMedica, Medico, Paciente, Personal
# from django.contrib.auth.admin import UserAdmin


# class UsuarioAdmin(UserAdmin):
#     model = Usuario

#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ("dni", "nombre", "apellidos", "fecha_nacimiento", "telefono", "ciudad",)}),
#     )
#     ordering = []
admin.site.register(PerfilUsuario)
admin.site.register(Paciente)
admin.site.register(Personal)
admin.site.register(Medico)
admin.site.register(CitaMedica)
admin.site.register(Especialidad)
# admin.site.register(Usuario, UsuarioAdmin)

# class PersonalAdmin(admin.ModelAdmin):
#     pass


# class PacienteAdmin(admin.ModelAdmin):
#     pass


# class MedicoAdmin(admin.ModelAdmin):
#     pass


# class CitaMedicaAdmin(admin.ModelAdmin):
#     pass
