import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "contratistas_project.settings")
django.setup()

from django.core.management import call_command

# Ejecuta las migraciones
call_command('migrate')
