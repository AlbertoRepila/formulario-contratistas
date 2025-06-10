from django.urls import path  #path se usa para definir rutas en Django
from . import views #importas views que contienen las funciones que se ejecutan cuando el usuario entra en una URL

urlpatterns = [  #url disponible dentro de mi app
    path('', views.mis_formularios, name='mis_formularios'),  #pagina de inicio del usuario, se muestra todos los formularios del suuario que ha iniciado sesión
    path('formulario/nuevo/', views.editar_formulario, name='nuevo_formulario'),  # crea un nuevo formulario, se ejecuta editar_formulario sin id
    path('formulario/<int:id>/', views.editar_formulario, name='editar_formulario'), #se accede a formulario ya creado y se da la posibilidad de editarlo
    path('exportar/', views.exportar_mis_formularios_excel, name='exportar_excel'), #para exportar el formulario excel por parte de los contratistas
    #path('crear-superusuario/', views.create_superuser, name='crear_superusuario'),
]


#si quiers añadir una nueva vista con boton y pantalla eprsonalidad, tendrias que añadir mas path aqui y su funcion en views
