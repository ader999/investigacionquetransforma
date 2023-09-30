from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required  # Importa el decorador de autenticación
from django.contrib import messages
from django.db.models import Avg
from django.http import FileResponse , HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO  # Importa BytesIO para trabajar con datos binarios
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle

from .models import Estudiante,Materia,Nota


def redirigir_a_blog(request):
    return redirect('blog_app')

def inicio(request):
    return render(request, 'inicio.html')

def acerca_de(request):
    return render(request,'acerca_de.html')

def contacto(request):
    return render(request,'contacto.html')





def notas(request):
    # Recuperar el código de carnet del estudiante desde la variable de sesión
    carnet = request.session.get('carnet', None)
    estudiantes = []

    if carnet:
        # Filtrar los estudiantes por carnet
        estudiantes = Estudiante.objects.filter(carnet=carnet)

        # Si se proporciona un carnet de estudiante en la URL, filtramos las notas por ese estudiante
        notas = Nota.objects.filter(estudiante_carnet__carnet=carnet)

    else:
        notas = []

    # Calcular el promedio de calificaciones para cada estudiante
    for estudiante in estudiantes:
        promedio_calificaciones = Nota.objects.filter(estudiante_carnet=estudiante).aggregate(Avg('calificacion'))
        estudiante.promedio_calificaciones = round(promedio_calificaciones['calificacion__avg'])

    context = {
        'estudiantes': estudiantes,
        'notas': notas,
    }
    return render(request, 'notas.html', context)

"""def notas(request):
    print("Carnet almacenado en la sesión:", request.session.get('carnet', None))

    # Recuperar el código de carnet del estudiante desde la variable de sesión
    carnet = request.session.get('carnet', None)
    # Si se proporciona un carnet de estudiante en la URL, filtramos las notas por ese estudiante
    notas = []

    if carnet:
        # Busca el estudiante por su carnet
        estudiante = Estudiante.objects.filter(carnet=carnet).first()

        if estudiante:
            # Si se encontró el estudiante, ahora puedes filtrar las notas por su relación con el estudiante
            notas = Nota.objects.filter(estudiante_carnet=estudiante)

    context = {
        'notas': notas,
    }

    return render(request, 'notas.html', context)
"""

def login(request):
    print("Me estoy ejecutando ")
    if request.method == 'POST':
        # Obtener los datos del formulario
        carnet = request.POST['username']
        contraseña = request.POST['password']

        # Buscar un estudiante con el carnet proporcionado
        estudiante = Estudiante.objects.filter(carnet=carnet).first()

        if estudiante is not None and estudiante.contraseña == contraseña:
            # Las credenciales son válidas, puedes agregar más lógica de autenticación si es necesario
            # Por ejemplo, aquí podrías iniciar sesión con tu propio sistema de autenticación si lo tienes
            # Agregar el código de carnet del estudiante a la variable de contexto
            request.session['carnet'] = carnet
            return redirect('notas')  # Redirigir a la página de notas o a la que desees
        else:
            # Las credenciales no son válidas, mostrar un mensaje de error
            messages.error(request, 'Código Carnet o contraseña incorrectos.')

    return render(request, 'login.html')


def generar_pdf(request):
    # Obtener el carnet del estudiante desde alguna fuente confiable, como la sesión
    carnet = request.session.get('carnet', None)

    if carnet:
        # Filtrar las notas por el carnet del estudiante
        notas = Nota.objects.filter(estudiante_carnet__carnet=carnet)
        estudiante = Estudiante.objects.get(carnet=carnet)

        if notas.exists():  # Verificar si hay notas para el estudiante
            # Crear un objeto BytesIO para almacenar los datos del PDF
            buffer = BytesIO()

            # Crear el objeto PDF utilizando el objeto BytesIO
            p = canvas.Canvas(buffer, pagesize=letter)

            # Agregar título al PDF con el nombre del estudiante
            p.setFont("Helvetica-Bold", 16)
            p.drawString(100, 750, f"Notas del estudiante: {estudiante.nombre} (Carnet: {carnet})")

            # Definir datos para la tabla y agregar encabezados
            data = [["#", "Materia", "Calificación"]]

            # Llenar la tabla con las notas del estudiante
            for i, nota in enumerate(notas, start=1):
                data.append([str(i), nota.materia.nombre, str(nota.calificacion)])

            # Configurar el estilo de la tabla
            width, height = letter
            table = Table(data, colWidths=[40, width / 2.5, width / 5])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),
                ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
                ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))
            ]))

            # Ajustar el tamaño y la posición de la tabla para que ocupe más espacio
            table.wrapOn(p, width - 100, height - 150)
            table.drawOn(p, 100, height - table._height - 70)

            # Cerrar el objeto PDF
            p.showPage()
            p.save()

            # Configurar el objeto BytesIO para que esté listo para ser leído
            buffer.seek(0)

            # Crear un objeto FileResponse con el tipo de contenido adecuado para PDF
            response = FileResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="notas.pdf"'

            return response

    # Si no se encontraron notas para el estudiante o no se proporcionó un carnet válido,
    # puedes devolver una respuesta que indica que no hay datos disponibles o manejarlo de otra manera según tus necesidades.

    return HttpResponse("No hay notas disponibles para este estudiante.")


