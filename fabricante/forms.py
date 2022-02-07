from django.forms import ModelForm
from .models import Fabricante


class FabricanteForm(ModelForm):
    class Meta:
        model = Fabricante
        fields = ('nome', 'ano_fundacao')
