from django.db import models
from django.urls import reverse

# Create your models here.
class Fabricante(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    ano_fundacao = models.IntegerField(verbose_name='Ano de Fabricação')

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('home_fabricantes')