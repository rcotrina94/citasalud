# -*- coding: utf-8 -*-
from django.db import migrations
import os
from django.core.management import call_command

fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
fixture_filename = 'admins.json'


def load_fixture(apps, schema_editor):
    fixture_file = os.path.join(fixture_dir, fixture_filename)
#    call_command('loaddata', fixture_file)


def unload_fixture(apps, schema_editor):
    "Brutally deleting all entries for this model..."

    MyModel = apps.get_model("citasalud", "Usuario")
    MyModel.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_especialidades'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
