from django.contrib import admin
from .models import Sala, Horario

# Register your models here.

class TermInlineAdmin(admin.TabularInline):
	model = Sala.horarios.through

class SalaAdmin(admin.ModelAdmin):
	inlines = (TermInlineAdmin,)

admin.site.register(Sala, SalaAdmin)
admin.site.register(Horario)
#admin.site.register(HorarioSala)
