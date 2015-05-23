#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "citasalud.settings")

from citasalud.apps.main.models import Usuario

superuser = Usuario.objects.create_user(
    username='admin',
    dni='76086783',
    first_name='Richard',
    last_name='Cotrina',
    fecha_nacimiento='1994-05-04',
)

superuser.set_password('admin')
superuser.save()

superuser.is_active = True
superuser.is_superuser = True
superuser.is_staff = True
superuser.save()