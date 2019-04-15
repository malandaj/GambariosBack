from django.db import models
from django.urls import reverse


class Gambario(models.Model):
    """
    Una clase definiendo un gambario
    """

    # Campos
    nombre = models.CharField(max_length=10, help_text="Nombre del gambario")
    habitantes = models.CharField(max_length=20, help_text="Habitantes del gambario")

    # Metadata
    class Meta:
        ordering = ["id"]

    # Método
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de Gambario.
        """
        return reverse('gambario-detail', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto Gambario (en el sitio de Admin, etc.)
        """
        return self.nombre


class TemperaturaManager(models.Manager):
    def create_temperatura(self, lectura, id_gambario):
        temperature = float(lectura)
        temperatura = self.create(temperatura=temperature, gambario_id=id_gambario)
        return temperatura


class Temperatura(models.Model):
    """
    Una clase definiendo una lectura de temperatura
    """

    # Campos
    temperatura = models.FloatField()
    gambario = models.ForeignKey(Gambario, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Manager
    objects = TemperaturaManager()
