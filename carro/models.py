from django.db import models
from fabricante.models import Fabricante
from django.urls import reverse

# Create your models here.
class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField()
    pais_origem = models.CharField(max_length=100)
    potencia_motor = models.IntegerField()
    fabricante = models.ForeignKey(Fabricante, null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return reverse('home_carros')

