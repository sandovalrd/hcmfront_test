from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .choices import *

# Create your models here.

class Sala(models.Model):
	nombre = models.CharField(max_length=50)
	ubicacion = models.CharField(max_length=50)
	capacidad = models.SmallIntegerField()
	horarios = models.ManyToManyField('Horario', 
		through='HorarioSala', 
		through_fields=('sala','horario'))

	class Meta:
		ordering = ['nombre']

	def __str__(self):
		return self.nombre

class Horario(models.Model):
	dia = models.IntegerField(choices=DIAS_CHOICES, default=1)
	descripcion = models.CharField(max_length=50)
	hora_inicio = models.SmallIntegerField(validators=[MaxValueValidator(20), MinValueValidator(8)])
	hora_fin = models.SmallIntegerField(validators=[MaxValueValidator(20), MinValueValidator(8)])

	class Meta:
		ordering = ['descripcion']

	def __str__(self):
		return self.descripcion

class HorarioSala(models.Model):
	sala = models.ForeignKey(Sala, related_name='membership')
	horario = models.ForeignKey(Horario, related_name='membership')
	estatus = models.IntegerField(choices=STATUS_SALA_CHOICES, default=1)

	class Meta:
		verbose_name = "Horarios de Sala"
		unique_together = ('sala', 'horario')
		auto_created = True

	def __str__(self):
		return "%s en el  horario de %s (Estatus %s)" % (self.sala, self.horario, self.estatus)
