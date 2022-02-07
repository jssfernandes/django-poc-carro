from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.views import View
from .models import Carro, Fabricante
from fabricante.forms import FabricanteForm
from carro.forms import CarroForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def home_fabricantes(request):
    fabricantes = Fabricante.objects.filter()
    data = {'fabricantes': fabricantes }
    for fabricante in fabricantes:
        print(fabricante.nome)

    return render(request, 'fabricantes.html', data)

def home_carros(request):
    carros = Carro.objects.filter()
    data = {'carros': carros }
    for carro in carros:
        print(carro.modelo)
        print(carro.potencia_motor)
    return render(request, 'carros.html', data)

class FabricanteIndex(ListView):
    model = Fabricante
    template_name = 'fabricantes.html'
    paginate_by = 10
    context_object_name = 'fabricantes'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('nome')
        # qs = qs.order_by('nome').filter()
        qs = qs.order_by('id').filter()
        return qs

class FabricanteCreate(CreateView):
    template_name = 'fabricante.html'
    model = Fabricante
    fields = ['nome', 'ano_fundacao']
    context_object_name = 'fabricante'

class FabricanteUpdate(UpdateView):
    template_name = 'editar_fabricante.html'
    model = Fabricante
    form_class = FabricanteForm
    context_object_name = 'fabricante'

class CarroIndex(ListView):
    model = Carro
    template_name = 'carros.html'
    paginate_by = 10
    context_object_name = 'carros'

    def get_queryset(self):
        qs = super().get_queryset()
        # qs = qs.select_related('modelo')
        qs = qs.order_by('id').filter()
        return qs

class CarroCreate(CreateView):
    template_name = 'carro.html'
    model = Carro
    fields = ['modelo', 'ano_fabricacao', 'pais_origem', 'potencia_motor', 'fabricante']
    context_object_name = 'carro'

class CarroUpdate(UpdateView):
    template_name = 'editar_carro.html'
    model = Carro
    form_class = CarroForm
    context_object_name = 'carro'