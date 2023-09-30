from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    lista_areasConocimiento = (
        ('Educacion', 'Educación, Humanidades y Artes'),
        ('Ciencia_Sociales', 'Ciencias Sociales, Económicas, Administrativas y Derecho'),
        ('Ciencias_de_la_vida', 'Ciencias de la Vida'),
        ('Fisica', 'Física'),
        ('Matematicas_Y_Estadisticas', 'Matemáticas y Estadísticas'),
        ('Ingenieria', 'Ingeniería, Industria, Arquitectura e Informática'),
        ('Ciencias_Agropecuarias_Ambientales', 'Ciencias Agropecuarias y Ambientales'),
        ('Salud_Servicios_sociales_Bienestar', 'Salud, Servicios Sociales y Bienestar'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='blog_pdfs/', blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100, null=False)
    categoria = models.CharField(max_length=255,choices=lista_areasConocimiento)

    def __str__(self):
        return self.title