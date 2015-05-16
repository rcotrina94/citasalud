# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CitaMedica',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('horario', models.DateTimeField(verbose_name=b'Hora de cita')),
            ],
            options={
                'verbose_name': 'Cita m\xe9dica',
                'verbose_name_plural': 'Citas m\xe9dicas',
            },
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.CharField(max_length=5, serialize=False, verbose_name=b'ID Especialidad', primary_key=True)),
                ('nombre', models.CharField(max_length=32, verbose_name=b'Nombre')),
            ],
            options={
                'ordering': ('id',),
                'verbose_name': 'Especialidad',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('nombre', models.CharField(max_length=32, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=32, verbose_name=b'Apellidos')),
                ('telefono', models.CharField(max_length=9, verbose_name=b'Tel\xc3\xa9fono')),
                ('nss', models.DecimalField(serialize=False, verbose_name=b'NSS', primary_key=True, decimal_places=0, max_digits=9)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32, verbose_name=b'Nombre')),
                ('apellidos', models.CharField(max_length=32, verbose_name=b'Apellidos')),
                ('telefono', models.CharField(max_length=9, verbose_name=b'Tel\xc3\xa9fono')),
                ('nregistropersonal', models.CharField(max_length=5, verbose_name=b'N\xc2\xb0 Registro personal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('personal_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='main.Personal')),
                ('ncolegiado', models.CharField(max_length=5, serialize=False, verbose_name=b'N\xc2\xb0 Colegiado', primary_key=True)),
                ('especialidades', models.ManyToManyField(related_name='especialidades', to='main.Especialidad', blank=True)),
            ],
            options={
                'ordering': ('ncolegiado',),
                'verbose_name': 'M\xe9dico',
                'verbose_name_plural': 'M\xe9dicos',
            },
            bases=('main.personal',),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='paciente',
            field=models.ForeignKey(to='main.Paciente'),
        ),
        migrations.AddField(
            model_name='citamedica',
            name='medico',
            field=models.ForeignKey(to='main.Medico'),
        ),
    ]
