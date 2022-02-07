from django.contrib import admin
from .models import Fabricante
# from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    list_display_links = ('id', 'nome')
    # list_editable = ('nome')
    list_per_page = 10
    
admin.site.register(Fabricante, FabricanteAdmin)