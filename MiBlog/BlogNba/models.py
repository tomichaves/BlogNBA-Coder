from django.conf import settings
from django.db import models
from django.utils import timezone

class Equipos(models.Model):
    ciudad = models.CharField(max_length=50, verbose_name='Nombre Ciudad')
    equipo = models.CharField(max_length=50,verbose_name='Nombre Equipo')

    def nombre_completo(self):
        return "{}, {}".format(self.ciudad, self.equipo)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name='Equipo'
        verbose_name_plural='Equipos'
        db_table='equios_nba'
        ordering=['ciudad','-equipo']

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    equipo = models.ForeignKey(Equipos, null=True, blank=True, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creado = models.DateTimeField(default = timezone.now)
    fecha_publicado = models.DateTimeField(blank = True, null = True)

    def publicar(self):
        self.fecha_publicado = timezone.now()
        self.save()

    def __str__(self):
        return f"Equipo:{self.equipo} -Titulo: {self.titulo}"

opciones_consultas = [
    [0,"consultar"],
    [1,"reclamar"],
    [2,"sugerir"],
    [3,"felicitar"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    numero = models.IntegerField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre