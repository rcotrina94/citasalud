# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import citasalud.apps.main.customfields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('dni', citasalud.apps.main.customfields.DNIField(max_length=8, unique=True, serialize=False, verbose_name=b'DNI', primary_key=True)),
                ('username', models.CharField(unique=True, max_length=16, verbose_name=b'Nombre de usuario')),
                ('first_name', models.CharField(max_length=32, verbose_name=b'Nombres')),
                ('last_name', models.CharField(max_length=16, verbose_name=b'Ap. Paterno')),
                ('apellido_materno', models.CharField(max_length=16, verbose_name=b'Ap. Materno')),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento')),
                ('telefono', models.CharField(max_length=9, verbose_name=b'Tel\xc3\xa9fono', blank=True)),
                ('ciudad', models.CharField(max_length=128, verbose_name=b'Ciudad de origen')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'E-mail', blank=True, null=True)),
                ('avatar', models.ImageField(default=b'/media/avatar/sin_imagen.png', upload_to=b'avatar', verbose_name=b'Imagen', blank=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.DateTimeField(verbose_name=b'Hora de cita')),
                ('asistio', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Cita m\xe9dica',
                'verbose_name_plural': 'Citas m\xe9dicas',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('nregistropersonal', models.DecimalField(serialize=False, verbose_name=b'N\xc2\xb0 Registro de Personal', primary_key=True, decimal_places=0, max_digits=9)),
                ('departamento', models.CharField(max_length=32, verbose_name=b'Departamento')),
                ('cargo', models.CharField(max_length=32, verbose_name=b'Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.CharField(max_length=5, serialize=False, verbose_name=b'ID Especialidad', primary_key=True)),
                ('nombre', models.CharField(max_length=128, verbose_name=b'Nombre')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_solitud', models.DateField(verbose_name=b'Fecha de Solicitud')),
                ('fecha_aplicacion', models.DateField(verbose_name=b'Fecha de aplicaci\xc3\xb3n')),
                ('observacion', models.CharField(max_length=256, verbose_name=b'Observacion')),
            ],
            options={
                'verbose_name': 'Examen',
                'verbose_name_plural': 'Ex\xe1menes',
            },
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('numero', models.CharField(max_length=5, serialize=False, verbose_name=b'N\xc2\xb0 H.C.', primary_key=True)),
            ],
            options={
                'verbose_name': 'Historia Cl\xednica',
                'verbose_name_plural': 'Historias Cl\xednicas',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nss', models.DecimalField(serialize=False, verbose_name=b'NSS', primary_key=True, decimal_places=0, max_digits=9)),
                ('usuario', models.OneToOneField(related_name='paciente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('documento', models.PositiveIntegerField(verbose_name=b'N\xc2\xb0 de Documento Asociado')),
                ('descripcion', models.CharField(max_length=256, verbose_name=b'Descripci\xc3\xb3n')),
                ('examen', models.ForeignKey(to='main.Examen')),
            ],
        ),
        migrations.CreateModel(
            name='TipoExamen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=64, verbose_name=b'Examen')),
                ('descripcion', models.CharField(max_length=128, verbose_name=b'Descripci\xc3\xb3n')),
            ],
            options={
                'verbose_name': 'Tipo de examen',
                'verbose_name_plural': 'Tipos de examen',
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('empleado_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='main.Empleado')),
                ('ncolegiado', models.PositiveIntegerField(verbose_name=b'N\xc2\xb0 Colegiado')),
                ('especialidades', models.ManyToManyField(related_name='especialidades', to='main.Especialidad', blank=True)),
            ],
            options={
                'ordering': ('ncolegiado',),
                'verbose_name': 'M\xe9dico',
                'verbose_name_plural': 'M\xe9dicos',
            },
            bases=('main.empleado',),
        ),
        migrations.AddField(
            model_name='historiaclinica',
            name='paciente',
            field=models.OneToOneField(to='main.Paciente'),
        ),
        migrations.AddField(
            model_name='examen',
            name='historia',
            field=models.ForeignKey(to='main.Paciente'),
        ),
        migrations.AddField(
            model_name='examen',
            name='tipo_examen',
            field=models.ForeignKey(to='main.TipoExamen'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='superior',
            field=models.ForeignKey(related_name='jefe', blank=True, to='main.Empleado', null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='usuario',
            field=models.OneToOneField(related_name='personal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='historia',
            field=models.ForeignKey(to='main.HistoriaClinica'),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='medico',
            field=models.ForeignKey(to='main.Medico'),
        ),
    ]
