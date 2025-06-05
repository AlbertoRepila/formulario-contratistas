
from django.http import HttpResponse
from django.contrib import admin
from .models import Formulario
from openpyxl import Workbook

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'completo', 'fecha_creacion')
    list_filter = ('completo', 'fecha_creacion')
    search_fields = ('usuario__username', 'nombre_proyecto', 'descripcion')
    actions = ['exportar_excel']

    def exportar_excel(self, request, queryset):
        wb = Workbook()
        ws = wb.active
        ws.title = "Formularios"

        # Cabecera
        ws.append(['ID', 'Usuario', 'Grupo', 'Nombre Proyecto', 'Completo', 'Fecha'])

        # Datos
        for f in queryset:
            ws.append([
                f.id,
                f.usuario.username,
                f.grupo.name if f.grupo else '',
                f.nombre_proyecto,
                'Sí' if f.completo else 'No',
                f.fecha_creacion.strftime('%Y-%m-%d %H:%M')
            ])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="formularios.xlsx"'
        wb.save(response)
        return response

    exportar_excel.short_description = "Exportar formularios seleccionados en Excel"
