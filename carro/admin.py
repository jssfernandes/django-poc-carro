from django.contrib import admin
from .models import Carro

# Register your models here.
class CarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'ano_fabricacao', 'potencia_motor', 'pais_origem', 'fabricante', )
    # list_editable = ('modelo',)
    list_display_links = ('id', 'modelo', )
    list_per_page = 10

admin.site.register(Carro, CarroAdmin)