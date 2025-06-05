from django.contrib import admin  #importa el panel de administración django
from django.urls import path, include #path para rutas especificas, include para usar rutas definidas en otro archivos, como los de mi app
from django.contrib.auth import views as auth_views #importa las vistas de login y logout que trae django por defecto

urlpatterns = [  #lista de urls que django utiliza para saber a donde mandarte cada vez, añadir aqui todas las nuevas
    path('admin/', admin.site.urls),
    path('formularios/', include('formularios.urls')),  #lista de formularios, crear nuevo formulario, editar formulario 
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  #pantalla de inicio de sesión. se activa automaticamente si no estas logueado
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'), #se te cierra la sesión y te lleva en funcion de lo que este en setings en logout_redirect
]
