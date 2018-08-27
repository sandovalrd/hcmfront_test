from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# Create your views here.

class RegisterUsers(CreateView):
	template_name = "users/register.html"
	form_class = RegisterForm
	success_url = reverse_lazy('login')

class Login(FormView):
	template_name = 'users/login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('reservar-list')

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(Login, self).form_valid(form)