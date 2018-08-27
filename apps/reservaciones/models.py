from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ..sala.models import Sala
from .choices import *
import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Insumo(models.Model):
	# Insumos de las salas
	descripcion = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Insumo"

	def __str__(self):
		return self.descripcion

class Reservar(models.Model):
	nombre = models.CharField(max_length=50)
	fecha_solicitud = models.DateField()
	hora_inicio = models.SmallIntegerField(validators=[MaxValueValidator(20), MinValueValidator(8)])
	hora_fin = models.SmallIntegerField(validators=[MaxValueValidator(20), MinValueValidator(8)])
	cantidad = models.SmallIntegerField(
		default=2,
		verbose_name='Cantidad de personas',
		validators=[MaxValueValidator(50), MinValueValidator(2)],)
	sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
	insumos = models.ManyToManyField(Insumo, default=(1,2))
	estatus = models.IntegerField(choices=STATUS_SOLICITUD_CHOICES, default=1)

	class Meta:
		verbose_name = "Reserva de salas"
		verbose_name_plural = "Reservar"
		ordering = ['fecha_solicitud']

	def __str__(self):
		return self.nombre
