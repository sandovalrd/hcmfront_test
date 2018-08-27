from django import forms
from .models import Reservar
from ..sala.models import Sala, HorarioSala
import datetime

class ResevarForm(forms.ModelForm):

	class Meta:
		model = Reservar
		fields = [
			'nombre',
			'sala',
			'cantidad',
			'fecha_solicitud',
			'hora_inicio',
			'hora_fin',
			'insumos',		]
		labels = {
			'nombre' : 'Nombre de la Solicitud: ',
			'sala' : 'Sala del evento: ',
			'cantidad' : 'Cantidad de personas: ',
			'fecha_solicitud' : 'Fecha del evento: ',
			'hora_inicio' : 'Hora inicio de la actividad: ',
			'hora_fin' : 'Hora fin de la actividad: ',
			'insumos' : 'Insumos requeridos: ',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control', "placeholder":"Curso de Django"}),
			'sala' : forms.Select(attrs={'class': 'form-control'}),
			'cantidad' : forms.NumberInput(attrs={'class': 'form-control'}),
			'fecha_solicitud' : forms.SelectDateWidget(),
			'hora_inicio' : forms.NumberInput(attrs={'class': 'form-control',"placeholder":"8"}),
			'hora_fin' : forms.NumberInput(attrs={'class': 'form-control',"placeholder":"18"}),
			'insumos' : forms.CheckboxSelectMultiple(),
		}


	def clean_fecha_solicitud(self):
		my_date = self.cleaned_data.get("fecha_solicitud")
		if my_date < datetime.date.today():
			msg = u"La fecha de solicitud no puede ser menor a la fecha de hoy!"
			self.add_error('fecha_solicitud', msg)
		return self.cleaned_data.get("fecha_solicitud")

class ResevarEstatusForm(forms.ModelForm):

	class Meta:
		model = Reservar
		fields = [
			'estatus',]
		labels = {
			'estatus' : 'Estatus ',
		}
		widgets = {
			'estatus' : forms.Select(attrs={'class': 'form-control'}),
		}