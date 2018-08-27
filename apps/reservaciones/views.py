from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# forms
from .forms import ResevarForm, ResevarEstatusForm
# models
from .models import Reservar
# time
import datetime

class ReservarList(LoginRequiredMixin,ListView):
	queryset = Reservar.objects.filter(fecha_solicitud__gte = datetime.datetime.now())[:20]

class ReservarDetail(LoginRequiredMixin,DetailView):
	model = Reservar

class ReservarDelete(LoginRequiredMixin,DeleteView):
	model = Reservar
	success_url = reverse_lazy('reservar-list')

class ReservarUpdate(LoginRequiredMixin,UpdateView):
	model = Reservar
	form_class = ResevarForm
	success_url = reverse_lazy('reservar-list')

class ReservarCreate(LoginRequiredMixin,CreateView):
	model = Reservar 
	#queryset = Reservar.objects.filter()
	form_class = ResevarForm
	success_url = reverse_lazy('reservar-list')

#Clases para el estatus de las reservas
class EstatusReserva(LoginRequiredMixin,ListView):
	queryset = Reservar.objects.filter(fecha_solicitud__gte = datetime.datetime.now())[:20]
	template_name = 'reservaciones/reservar_estatus_list.html'

class CambiarEstatusReserva(LoginRequiredMixin,UpdateView):
	model = Reservar
	form_class = ResevarEstatusForm
	template_name = 'reservaciones/reservar_estatus_form.html'
	success_url = reverse_lazy('reservar-estatus-list')

class ReservarEstatusDetail(LoginRequiredMixin,DetailView):
	model = Reservar
	template_name = 'reservaciones/reservar_estatus_detail.html'

