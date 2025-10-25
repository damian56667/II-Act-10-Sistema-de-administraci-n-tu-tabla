from django.db import models

class Autor(models.Model):
    autor_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    bibliografia = models.TextField()
    pagina_web = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
