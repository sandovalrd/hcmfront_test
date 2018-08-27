from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# forms
from .forms import SalaForm, InsumoForm, HorarioForm
# models
from .models import Sala, Horario, HorarioSala
from ..reservaciones.models import Insumo


# Clases para las Salas
class SalaList(LoginRequiredMixin,ListView):
	queryset = Sala.objects.all()

class SalaDetail(LoginRequiredMixin,DetailView):
	model = Sala
	def get_context_data(self, **kwargs):
		context = super(SalaDetail, self).get_context_data(**kwargs)
		objeto = super(SalaDetail, self).get_object()
		context['disponibilidad_list'] = HorarioSala.objects.filter(sala_id=objeto.id)
		return context	

class SalaDelete(LoginRequiredMixin,DeleteView):
	model = Sala
	success_url = reverse_lazy('sala-list')

class SalaUpdate(LoginRequiredMixin,UpdateView):
	model = Sala
	form_class = SalaForm
	success_url = reverse_lazy('sala-list')

class SalaCreate(LoginRequiredMixin,CreateView):
	model = Sala.horarios.through
	form_class = SalaForm
	success_url = reverse_lazy('sala-list')

class HorarioCreate(LoginRequiredMixin,CreateView):
	model = Sala 
	#form_class = HorarioForm
	template_name = 'sala/horario_form.html'
	success_url = reverse_lazy('sala-list')

# Clases para los Insumos
class InsumoList(LoginRequiredMixin,ListView):
	model = Insumo

class InsumoDelete(LoginRequiredMixin,DeleteView):
	model = Insumo
	success_url = reverse_lazy('insumo-list')

class InsumoCreate(LoginRequiredMixin,CreateView):
	model = Insumo
	form_class = InsumoForm
	success_url = reverse_lazy('insumo-list')

class InsumoUpdate(LoginRequiredMixin,UpdateView):
	model = Insumo
	form_class = InsumoForm
	success_url = reverse_lazy('insumo-list')

# Clases para los Horarios
class HorarioList(LoginRequiredMixin,ListView):
	model = Horario

class HorarioDelete(LoginRequiredMixin,DeleteView):
	model = Horario
	success_url = reverse_lazy('horario-list')

class HorarioCreate(LoginRequiredMixin,CreateView):
	model = Horario
	form_class = HorarioForm
	success_url = reverse_lazy('horario-list')

class HorarioUpdate(LoginRequiredMixin,UpdateView):
	model = Horario
	form_class = HorarioForm
	success_url = reverse_lazy('horario-list')