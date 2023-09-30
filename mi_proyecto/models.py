from django.db import models

class Estudiante(models.Model):
    nombre= models.CharField(max_length=100,null=False,unique=True,verbose_name='Nombre')
    contraseña = models.CharField(max_length=20,null=False,unique=False,verbose_name='Contraseña')
    carnet = models.CharField(max_length=20,null=False,unique=True,verbose_name='Carnet')

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table= "estudiantes"
        verbose_name= "Estudainte"
        verbose_name_plural = "Estudiantes"
        ordering = ['id'] #ordenar asendente mente

class Materia(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Nota(models.Model):
    materia= models.ForeignKey(Materia,on_delete=models.CASCADE)
    estudiante_carnet = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    calificacion = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return f"{self.materia.nombre} - {self.estudiante_carnet.nombre}"
        #return f"{self.materia} - {self.estudiante_carnet}"