import csv
from formularios.models import Formulario

with open('formularios_export.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'ID', 'Usuario', 'Grupo' ,'Nombre del proyecto', 'Descripción',
        'Nº de trabajadores', 'Peso residuo (kg)', 'Fecha inicio',
        'Fecha revisión', '¿Peligroso?', 'Tipo de residuo', '¿Completo?',
        'Fecha creación', 'Última modificación'
    ])

    for f in Formulario.objects.all():
        writer.writerow([
            f.id,
            f.usuario.username,
            f.grupo.name,
            f.nombre_proyecto,
            f.descripcion,
            f.cantidad_trabajadores,
            f.peso_residuo,
            f.fecha_inicio,
            f.fecha_revision,
            f.es_peligroso,
            f.get_tipo_residuo_display(),  # texto legible
            f.completo,
            f.fecha_creacion,
            f.ultima_modificacion,
        ])
