# coding=utf-8

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import (Usuario, Especialidad, CitaMedica, Medico,
                     Paciente, Empleado, HistoriaClinica, Examen,
                     TipoExamen,)

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('dni', 'username')

    def clean_password2(self):
        # Verificar si las contraseñas coinciden
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("La contraseña de confirmación no coindice.")
        return password2

    def save(self, commit=True):
        # Guardar la contraseña en formato no plano.
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = ('email', 'password', 'first_name', 'last_name', 'apellido_materno')

    def clean_password(self):
        # Reiniciar la contraseña
        return self.initial["password"]


class UsuarioAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # Campos a mostrar al listar los Usuarios.
    list_display = ('username', 'nombre_completo', 'email','is_superuser')
    list_filter = ('is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'avatar',)}),
        (u'Información Personal', {'fields': ('first_name','last_name','apellido_materno','telefono', 'fecha_nacimiento', 'ciudad')}),
        ('Permissions', {'fields': ('groups','is_superuser', 'is_active', 'is_staff',)}),
    )

    # Mostrar primero éstos campos al crear un Usuario.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'dni', 'first_name', 'last_name', )}
        ),
    )
    search_fields = ('username',)
    ordering = ('dni',)
    filter_horizontal = ()


admin.site.register(Usuario, UsuarioAdmin)
#admin.site.unregister(Group)
admin.site.register(Especialidad)
admin.site.register(CitaMedica)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Empleado)
admin.site.register(HistoriaClinica)
admin.site.register(Examen)
admin.site.register(TipoExamen)
