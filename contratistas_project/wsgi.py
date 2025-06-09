import os
from django.core.wsgi import get_wsgi_application
import django

# Configura el entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contratistas_project.settings')

# Inicia Django
django.setup()

# Importa el modelo de usuario
from django.contrib.auth.models import User

# Función para crear el superusuario si no existe
def create_superuser():
    username = 'admin'  # Cambia esto por el nombre de usuario que deseas
    password = 'password123'  # Cambia esto por una contraseña segura
    email = 'admin@example.com'  # Cambia esto por el correo electrónico del superusuario

    # Verifica si el superusuario ya existe
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuario {username} creado con éxito.")
    else:
        print(f"El superusuario {username} ya existe.")

# Crea el superusuario al iniciar la aplicación
create_superuser()

# Conexión a la base de datos desde las variables de entorno
DATABASES = {
    'default': dj_database_url.config(
        default=f"postgres://{os.environ['DATABASE_USER']}:{os.environ['DATABASE_PASSWORD']}@{os.environ['DATABASE_HOST']}:{os.environ['DATABASE_PORT']}/{os.environ['DATABASE_NAME']}"
    )
}

# Inicializa la aplicación Django
application = get_wsgi_application()


#WSGI: web server gategay interface. es el punto de entrada de django para servidores web, no es necesario tocarlo para desarrollo local
