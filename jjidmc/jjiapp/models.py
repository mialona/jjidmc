from django.db import models

class Configuracion(models.Model):
  fechas = models.CharField(max_length=255, blank=True)
  participacion = models.TextField(blank=True)
  formato = models.TextField(blank=True)
  periodo_inscripcion = models.CharField(max_length=255, blank=True)
  url_inscripcion = models.CharField(max_length=255, blank=True)

  def __str__(self):
    return f"Configuración"

class Edicion(models.Model):
  curso = models.CharField(max_length=4)
  titulo = models.CharField(max_length=255)
  descripcion = models.TextField(blank=True)
  parners = models.TextField(blank=True)

  def __str__(self):
    return f"{self.curso}"

class Presentacion(models.Model):
  edicion = models.ForeignKey(Edicion, on_delete=models.CASCADE)
  fecha = models.DateField()
  hora_inicio = models.TimeField()
  hora_fin = models.TimeField()
  titulo = models.CharField(max_length=255)
  autor = models.CharField(max_length=255, blank=True)
  keywords = models.TextField(blank=True)
  abstract = models.TextField(blank=True)
  destacado = models.BooleanField(default=False)
  sin_detalles = models.BooleanField(default=False)
  pdf = models.FileField(upload_to='pdf', null=True, blank=True)

  def __str__(self):
    return f"{self.titulo} {self.autor} {self.edicion.curso}"