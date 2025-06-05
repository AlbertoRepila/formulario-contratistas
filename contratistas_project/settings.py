from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent #el path coge la ruta del archivo actual (settings), .resolve obtiene la ruta absoluta .parent.parent sube 2 niveles hasta la raiz del proyecto. sirve para construir rutas relativas como la base de datos, estaticos, plantillas.etc...

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-devkey')  #es la clave secreta, para cookies, tokens CSRF, firmar sesiones. nunca publicar

DEBUG = os.environ.get('DEBUG', 'False') == 'True' #true muestra errores, falso no. a la hora de publicarlo cambiarlo a falso

ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1'] #que dominios pueden acceder a la web, en producción puede estar vacio, pero despues hay que rellenarlo  ['midominio.com', '127.0.0.1']

INSTALLED_APPS = [
    'formularios',  # Tu app personalizada
    'django.contrib.admin',         # Panel de administración
    'django.contrib.auth',          # Sistema de usuarios
    'django.contrib.contenttypes',  # Manejo de tipos de contenido
    'django.contrib.sessions',      # Soporte para sesiones
    'django.contrib.messages',      # Sistema de mensajes (ej. flash)
    'django.contrib.staticfiles',   # Archivos estáticos (CSS, JS, etc.)
]
 

MIDDLEWARE = [  #son capas intermedias que procesan peticiones y respuestas. Seguridad (cors, xss), manejo de sesiones y autenticación, protección contra CSRF, bloqueo de "clickjacking"
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'contratistas_project.urls' #el archivo principal de rutas es urls

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  #usa el motor de plantillas django
        'DIRS': [],  #incluir carpetas extras html si quieres
        'APP_DIRS': True,   #busca plantillas dentro de cada app (templates/)
        'OPTIONS': {
            'context_processors': [ #añade variabels automaticas a las plantillas (como user o request)
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'contratistas_project.wsgi.application'  #indica el punto de entrada del servidor web, solo relevante en producción

DATABASES = {  #base de datos
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []  #validadores de contraseña, que no sea muy corta, ni muy comun, ni solo numerica...

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True     # Activar sistema de traducción

USE_TZ = True       # Guardar en UTC, mostrar en tu zona

STATIC_URL = 'static/'  #define la url donde buscara elementos estaticos, como imagenes

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  #usar este campo como clave primaria (id) por defecto en nuevos modelos

LOGIN_URL = 'login'  #a donde vas si no estas logueado
LOGIN_REDIRECT_URL = '/formularios/' #a donde vas despues de iniciar sesión
LOGOUT_REDIRECT_URL = 'login' # a donde vas despues de cerrar sesión
