from django.db import models
from django.contrib.auth.models import User, Group

class Formulario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Solo verá sus formularios, cada formulario pertenece a un solo usuario. si borras el usuario borras los formularios

    #0 para ver que grupo de usuario es, cobra solo ve cobra y enitec solo ve a enitec. cada formulario pertenece a un grupo
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE) 

    # 1. Texto corto
    nombre_proyecto = models.CharField("Nombre del proyecto", max_length=100)

    # 2. Texto largo
    descripcion = models.TextField("Descripción del proyecto", blank=True)

    # 3. Número entero
    cantidad_trabajadores = models.IntegerField("Nº de trabajadores", default=0)

    # 4. Número decimal
    peso_residuo = models.DecimalField("Peso estimado del residuo (kg)", max_digits=6, decimal_places=2)

    # 5. Fecha
    fecha_inicio = models.DateField("Fecha de inicio")

    # 6. Fecha y hora
    fecha_revision = models.DateTimeField("Fecha y hora de revisión", auto_now_add=True)

    # 7. Sí / No
    es_peligroso = models.BooleanField("¿Es un residuo peligroso?", default=False)

    #código ler
    #codigo_ler = models.CharField(
     #   "Código LER",
      #  max_length=6,
       # choices=[
        #    '111111',
         #   '222222'
          #  '333333'
      #  ]
    #)

    # 8. Opciones (choice)
    tipo_residuo = models.CharField(
        "Tipo de residuo",
        max_length=50,
        choices=[
            ('organico', 'Orgánico'),
            ('inerte', 'Inerte'),
            ('peligroso', 'Peligroso'),
        ]
    )

    # 9. Subida de archivo (PDF, imagen, etc.)
    documento = models.FileField("Documento adjunto", upload_to='documentos/', blank=True)

    # 10. Campo para saber si está completo o no
    completo = models.BooleanField(default=False)

    fecha_creacion = models.DateTimeField(auto_now_add=True) #campos que se rellenan automaticamente al completar el formulario
    ultima_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_proyecto} - {self.usuario.username}"
