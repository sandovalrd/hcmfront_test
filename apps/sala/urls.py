from django.conf.urls import url
from .views import *


urlpatterns = [

	# Salas
	url(r'^list/$', SalaList.as_view(), name='sala-list'),
	url(r'^detail/(?P<pk>[0-9]+)/$', SalaDetail.as_view(), name='sala-detail'),
	url(r'^delete/(?P<pk>[0-9]+)/$', SalaDelete.as_view(), name='sala-delete'),
	url(r'^update/(?P<pk>[0-9]+)/$', SalaUpdate.as_view(), name='sala-update'),
	url(r'^create/$', SalaCreate.as_view(), name='sala-create'),

	# Horarios
	url(r'^horarios/list/$', HorarioList.as_view(), name='horario-list'),
	url(r'^horarios/delete/(?P<pk>[0-9]+)/$', HorarioDelete.as_view(), name='horario-delete'),
	url(r'^horarios/update/(?P<pk>[0-9]+)/$', HorarioUpdate.as_view(), name='horario-update'),
	url(r'^horarios/create/$', HorarioCreate.as_view(), name='horario-create'),

	# Insumos
	url(r'^insumos/list/$', InsumoList.as_view(), name='insumo-list'),
	url(r'^insumos/delete/(?P<pk>[0-9]+)/$', InsumoDelete.as_view(), name='insumo-delete'),
	url(r'^insumos/update/(?P<pk>[0-9]+)/$', InsumoUpdate.as_view(), name='insumo-update'),
	url(r'^insumos/create/$', InsumoCreate.as_view(), name='insumo-create'),
]