import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contratistas_project.settings')

application = get_wsgi_application()

#WSGI: web server gategay interface. es el punto de entrada de django para servidores web, no es necesario tocarlo para desarrollo local
