from django.contrib.auth.decorators import login_required  #hace que si un usuario no haya iniciado sesion le redirige al principio
from django.shortcuts import render, get_object_or_404, redirect  #render carga plantilla html y le pasa datos. get_object... busca un objeto en la base de datos y sino lanza error 404, redirect le manda a otra pagina despues de haber iniciado seison
from .models import Formulario  #importa el modelo formulario para pdoer trabajar con el (leer, guardar, filtrar)
from .forms import FormularioForm #importa el formulario web que se basa en ese modelo, y que definistes en forms.py
import re  # ← para usar expresiones regulares como re.match()
from django.contrib.auth.models import Group  # ← para crear o consultar grupos
from openpyxl import Workbook
from django.http import HttpResponse
from django.core.management import call_command


@login_required #obliga q ue se tenga q hacer login
def mis_formularios(request):
    grupo_usuario = request.user.groups.first()  # Obtiene el primer grupo al que pertenece el usuario (cobra, enitec...)
    formularios = Formulario.objects.filter(grupo=grupo_usuario) #busca los usuarios creados por el y por su grupo
    return render(request, 'formularios/mis_formularios.html', {'formularios': formularios}) #muestra el html con la lista de formularios


@login_required
def editar_formulario(request, id=None):
    if id:
        formulario = get_object_or_404(Formulario, pk=id, usuario=request.user) #si hay un ID lo busca en la base de datos, sino aparece que no esta y da error
    else:
        formulario = Formulario(usuario=request.user) #si no hya crea uno en blanco y le asigna el usuario actual

    if request.method == 'POST':  #si hizo clic en enviar se guarda en la base de datos
        form = FormularioForm(request.POST, request.FILES, instance=formulario) #instance=formulario por si lo esta editando y ya existia
        if form.is_valid():
            formulario = form.save(commit=False)
            #👇 EXTRAE EL GRUPO desde el nombre del usuario (ej: 'cobra123' → 'cobra')
            nombre_usuario = request.user.username
            nombre_grupo = re.match(r'[a-zA-Z]+', nombre_usuario).group().lower()

            # 👇 Crea el grupo si no existe
            grupo, _ = Group.objects.get_or_create(name=nombre_grupo)

            # 👇 Añade el usuario al grupo si aún no está
            if not request.user.groups.filter(name=nombre_grupo).exists():
                request.user.groups.add(grupo)

            # 👇 Asigna el grupo al formulario
            formulario.grupo = grupo

            formulario.grupo = request.user.groups.first()  # ← 👈 aquí se asigna el grupo automáticamente
            formulario.save()
            return redirect('mis_formularios')
    else:
        form = FormularioForm(instance=formulario)

    return render(request, 'formularios/formulario.html', {'form': form})

@login_required
def exportar_mis_formularios_excel(request):
    grupo_usuario = request.user.groups.first()
    formularios = Formulario.objects.filter(grupo=grupo_usuario)

    wb = Workbook()
    ws = wb.active
    ws.title = "Mis Formularios"

    ws.append(['ID', 'Usuario', 'Grupo', 'Nombre Proyecto', 'Completo', 'Fecha'])

    for f in formularios:
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
    response['Content-Disposition'] = 'attachment; filename="mis_formularios.xlsx"'
    wb.save(response)
    return response

@login_required
def run_migrate(request):
    try:
        call_command('migrate')  # Ejecuta las migraciones
        return HttpResponse("Migraciones ejecutadas correctamente.")
    except Exception as e:
        return HttpResponse(f"Error al ejecutar migraciones: {str(e)}")


