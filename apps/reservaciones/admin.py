from django.contrib import admin
from .models import Reservar, Insumo

# Register your models here.

class ReservasAdmin(admin.ModelAdmin):
	ordering = ('nombre',)
	filter_vertical =  ('insumos',)

# Fue agregado temporalmente para verificar el modelo
admin.site.register(Reservar, ReservasAdmin)
admin.site.register(Insumo)