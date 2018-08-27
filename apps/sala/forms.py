from django import forms
from .models import Sala, Horario
from ..reservaciones.models import Insumo
from .choices import *

class SalaForm(forms.ModelForm):

	class Meta:
		model = Sala
		fields = [
			'nombre',
			'ubicacion',
			'capacidad',
			'horarios',		]
		labels = {
			'nombre' : 'Nombre de la Sala ',
			'ubicacion' : 'Ubicacacion ',
			'capacidad' : 'Capacidad ',
			'horarios' : 'Horarios ',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
			'ubicacion' : forms.TextInput(attrs={'class': 'form-control'}),
			'capacidad' : forms.NumberInput(attrs={'class': 'form-control'}),
			'horarios' : forms.CheckboxSelectMultiple(),
		}

class InsumoForm(forms.ModelForm):

	class Meta:
		model = Insumo
		fields = [
			'descripcion',	]
		labels = {
			'descripcion' : 'Nombre del Insumo ',
		}
		widgets = {
			'descripcion' : forms.TextInput(attrs={"class": "form-control", "placeholder":"Indique el nombre del insumo"}),
		}

class HorarioForm(forms.ModelForm):

	class Meta:
		model = Horario
		fields = [
			'dia',
			'descripcion',
			'hora_inicio',
			'hora_fin',		]
		labels = {
			'dia' : 'Dia de la semana ',
			'descripcion' : 'Descripcion del horario ',
			'hora_inicio' : 'Hora inicio ',
			'hora_fin' : 'Hora fin ',
		}
		widgets = {
			'dia' : forms.Select(attrs={'class': 'form-control'}),
			'descripcion' : forms.TextInput(attrs={"class": "form-control", "placeholder":"Ejmplo: Lunes de 8 a 10"}),
			'hora_inicio' : forms.NumberInput(attrs={"class": "form-control","placeholder":"8"}),
			'hora_fin' : forms.NumberInput(attrs={"class": "form-control","placeholder":"10"}),
		}