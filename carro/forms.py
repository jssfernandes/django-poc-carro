from django.forms import ModelForm
from .models import Carro


class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ('modelo', 'ano_fabricacao', 'pais_origem', 'potencia_motor', 'fabricante')
